import os
import sys
import logging
from game.player import Player
from game.nodes import Node

# path for node folder in root project directory
NODE_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "nodes")

class Game:
    def __init__(self):
        self.name = "Azurite - The Game"
        self.nodes = Node(NODE_PATH) # System for handling nodes
        self.player = None # Player object
        
    def __str__(self):
        return self.name
    
    # create player
    def create_player(self, name, health, mana, stamina):
        # create player
        player = Player(name, health, mana, stamina)
        # lets set a name
        player.set_name(name)
        # return player
        return player
    
    def start(self):
        # load nodes
        self.nodes.load_nodes(NODE_PATH)
        
        # create player
        name = input("Enter your name: ")
        self.player = self.create_player(name, 100, 100, 100)

        # game loop
        self.game_loop()

    def game_loop(self):
        node = self.nodes.display_menu()
