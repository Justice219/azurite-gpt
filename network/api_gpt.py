import os
import openai
import asyncio

# load environment variables
class GPT:
    def __init__(self):
        self.api_key = os.getenv("OPENAI_API_KEY")
        self.assistants = {}
        self.client = openai.Client(api_key=self.api_key)


    # ASSISTANTS API
    async def create_assistant(self, name, description=""):
        self.assistants[name] = self.client.beta.assistants.create(
            name = name,
            description = description,
            model = "gpt-3.5-turbo"
        )

        # create a thread for the assistant
        thread = self.client.beta.threads.create()
        self.assistants[name].thread_id = thread.id

    async def create_assistant_message(self, assistant, message, role):
        thread_id = self.assistants[assistant].thread_id
        message = self.client.beta.threads.messages.create(
            thread_id = thread_id,
            role = role,
            content = message
        )

    async def run_assistant_thread(self, assistant, instructions=""):
        thread_id = self.assistants[assistant].thread_id
        run = self.client.beta.threads.runs.create(
            thread_id = thread_id,
            assistant_id = self.assistants[assistant].id,
            instructions = instructions
        )

        return run.id

    async def reset_assistant_thread(self, assistant):
        thread_id = self.assistants[assistant].thread_id
        self.client.beta.threads.delete(thread_id)

        thread = self.client.beta.threads.create()
        self.assistants[assistant].thread_id = thread.id

    async def retrieve_assistant_message(self, assistant):
        messages = self.client.beta.threads.messages.list(
            thread_id = self.assistants[assistant].thread_id
        )

        # return the last message
        return messages

    async def run_assistant_check(self, run_id, name):
        while True:
            run = self.client.beta.threads.runs.retrieve(
                run_id = run_id,
                thread_id=self.assistants[name].thread_id
            )
            print("run status: ", run.status)
            if run.status == "complete":
                # get the last message
                message = await self.retrieve_assistant_message(name)
                return message
            if run.status == "failed":
                # get the last message
                message = await self.retrieve_assistant_message(name)
                print("Run Failed: " + run.last_error.message)
                return message
            
            await asyncio.sleep(1)
            await self.run_assistant_check(run_id, name)
        


    async def delete_assistant(self, name):
        openai.Assistant.delete(name)

    async def get_assistant(self, name):
        return openai.Assistant.retrieve(name)
    # END ASSISTANTS API

    # COMPLETION API
    async def create_completion(self, model, messages):
        response = self.client.chat.completions.create(
            model = model,
            messages = messages
        )

        return response, response.choices[0].message

    # END COMPLETION API


async def test_gpt():
    gpt = GPT()
    response, message = await gpt.create_completion(
        "gpt-3.5-turbo",
        [
            {
                "role": "system",
                "content": "You are a helpful assistant."
            },
            {
                "role": "user",
                "content": "What is your name?"
            }
        ]
    )
    print(message)



asyncio.run(test_gpt())


