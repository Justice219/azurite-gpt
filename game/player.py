import os
import sys
import logging
from game.entity import EntityBase

class Player(EntityBase):
    def __init__(self, name, health, mana, stamina):
        super().__init__(name, {
            "health": health,
            "mana": mana,
            "stamina": stamina
        })

    def __str__(self):
        return f"{self.name} - {self.vars}"

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name
    