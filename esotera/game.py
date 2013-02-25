from collections import deque

class Game:
    """The Esotera game engine"""

    def __init__(self):
        """Initialize the datastructures to be used in the game."""
        self.event_queue = deque() 
        self.actors = list()
        self.resources = list()
    
    def new_game(self):
        """Populates the game world and start the game"""
        pass

    def start(self):
        """Start the game."""
        pass

