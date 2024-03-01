import json
import os
import glob

class Node:
    def __init__(self, path):
        self.connections = {}
        self.current_node = None

    def add_connection(self, direction, node):
        self.connections[direction] = node

    def get_connection(self, direction):
        return self.connections.get(direction)

    # load nodes from json files in a directory
    def load_nodes(self, directory):
        for file_path in glob.glob(directory + "/*.json"):
            with open(file_path) as f:
                data = json.load(f)
                for node in data:
                    # create node
                    n = Node(node["name"], node["description"])
                    # add connections
                    for direction, connection in node["connections"].items():
                        n.add_connection(direction, connection)
                    # add node to nodes
                    self.nodes.append(n)
        
        # set current node
        self.current_node = self.nodes[0]

    # get node by name
    def get_node(self, name):
        for node in self.nodes:
            if node.get_name() == name:
                return node
        return None

    # get nodes
    def get_nodes(self):
        return self.nodes
    
    # function for handling node movement
    def move(self, direction):
        node = self.get_connection(direction)
        if node:
            self.current_node = node
            return node
        else:
            return None
        
    # function for getting current node
    def get_current_node(self):
        return self.current_node

    # display node menu
    def display_menu(self):
        # clear screen
        os.system("clear")
        # print menu
        print("What would you like to do?")
        # current node
        print(f"Current Node: {self.current_node.get_name()}")
        # display connections
        print("Connections:")

        cur_num = 1
        for direction, node in self.current_node.connections.items():
            print(f"{cur_num}. {direction} - {node}")
            cur_num += 1

        print(f"{cur_num}. Quit")
        # input
        choice = int(input("Choice: "))
        # check if choice is valid
        if choice > 0 and choice < cur_num:
            # get direction
            direction = list(self.current_node.connections.keys())[choice - 1]
            # move
            node = self.move(direction)

            return node
        else:
            print("Invalid choice")
            # reprint menu
            self.display_menu()

                
    # example json file
    # [
    #     {
    #         "name": "node1",
    #         "description": "This is node 1",
    #         "connections": {
    #             "north": "node2",
    #             "south": "node3"
    #         }
    #     },
    #     {
    #         "name": "node2",
    #         "description": "This is node 2",
    #         "connections": {
    #             "south": "node1"
    #         }
    #     },
    #     {
    #         "name": "node3",
    #         "description": "This is node 3",
    #         "connections": {
    #             "north": "node1"
    #         }
    #     }
    # ]
    #
                    