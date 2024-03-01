# Entity base 

import os
import sys

class EntityBase:
    def __init__(self, name, vars):
        self.name = name or "Entity"
        self.vars = vars or {}

        # create vars
        self.create_vars(vars)

    def __str__(self):
        return self.name

    def create_vars(self, vars):
        for key, value in vars.items():
            self[key] = value
        
    def __getvar__ (self, var):
        return self.vars.get(var)

    def __setvar__ (self, var, value):
        self.vars[var] = value

    def __delvar__ (self, var):
        del self.vars[var]

    # entity methods to be overriden
    def attack(self, target):
        pass

    def defend(self, target):
        pass

    def move(self, direction):
        pass






# Example enity usage

#class Player(EntityBase):
#    def __init__(self, name, vars):
#        super().__init__(name, vars)
#        self.vars = vars or {
#            "health": 100,
#            "mana": 100,
#            "stamina": 100
#        }#
#
#    def __str__(self):
#        return f"{self.name} - {self.vars}"

