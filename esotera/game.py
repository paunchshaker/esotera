"""This module contains basic code for running the game simulation"""

from collections import deque
from esotera.actor import Actor
from esotera.resource import Resource
import random

class Game:
    """The Esotera game engine"""

    def __init__(self):
        """Initialize the datastructures to be used in the game."""
        self.event_queue = deque() 
        self.actors = list()
        self.resources = list()
        self.turn = 0
    
    def new_game(self, number_actors = 5, number_turns = None):
        """Populates the game world and start the game"""
        current_turn = 0
        while current_turn < number_actors:
            actor_resources = {}
            for res_type in ['money', 'food', 'influence', 'shelter']:
                amount = random.randrange(1, 25)
                res = Resource( res_type, amount)
                actor_resources[res] = res
            self.actors.append( Actor(resources = actor_resources) )
            current_turn += 1
        self.start(number_turns)

    def start(self, turns = None):
        """Start the game."""
        self.turn = 0
        #display starting actors and their resources
        for actor in self.actors:
            print(str(actor))
        while turns == None or self.turn < turns:
            self.turn += 1
            for actor in self.actors:
                actor.take_turn(self.actors)
            print("Turn {0} complete!".format(str(self.turn)))
            command = input("Press enter for next turn, type p to print actors, or type q to end: ")
            command = command.strip().lower()
            if command == "p":
                for actor in self.actors:
                    print(str(actor))
                input()
            elif command == "q":
                break

