from collections import deque
from esotera.actor import Actor
from esotera.resource import Resource
from esotera.event import Event

class Game:
    """The Esotera game engine"""

    def __init__(self):
        """Initialize the datastructures to be used in the game."""
        self.event_queue = deque() 
        self.actors = list()
        self.resources = list()
        self.turn = 0
    
    def new_game(self, number_actors = 5, number_turns = 10):
        """Populates the game world and start the game"""
        self.actors = [Actor() for x in range(number_actors)]
        self.start(number_turns)

    def start(self, turns = None):
        """Start the game."""
        self.turn = 0
        while turns == None or self.turn < turns:
            self.turn += 1
            for actor in self.actors:
                actor.take_turn()
            print("Turn {0} complete!".format(str(self.turn)))

