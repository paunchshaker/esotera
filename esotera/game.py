from collections import deque

class Game:
    """The Esotera game engine"""

    def __init__(self):
        """This initializes the datastructures to be used in the game"""
        self.event_queue = deque() 
        self.actors = list()
        self.resources = list()
    
    def new_game(self):
        """This populates the game world and starts the game"""
        pass

    def start(self):
        pass

