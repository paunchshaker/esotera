import random
import copy
from esotera.resource import Resource

class Actor:
    """The actor class is the base class for entities that can perform actions.
    They are not necessarily organic (i.e. they might represent political,
            religious or social bodies)."""
    
    #class variables 
    number = 0

    def __init__(self, name = None, resources = dict()):
        """Initialize a new Actor."""
        if name:
            self.name = name
        else:
            Actor.number += 1
            self.name = "Actor" + str(Actor.number)
        self.resources = dict(resources)
    def offer(self, target, give, receive):
        """Offer an exchange (possibly one-sided) of resources."""
        accepts = target.accept(source = self, give = receive, receive = give)
        if accepts:
            self.exchange(target = target, give = give, receive = receive)
        else:
            #offer rejected, update AI accordingly
            pass
    def exchange(self, target, give, receive):
        """Exchange resources between Actors."""
        #exchange resources here
        if give:
            try:
                self.resources[give.kind] -= give
            except KeyError:
                self.resources[give.kind] = Resource(give.kind, 0)
                self.resources[give.kind] -= give
            try:
                target.resources[give.kind] += give
            except KeyError:
                target.resources[give.kind] = copy.copy(give)
        if receive:
            try:
                self.resources[receive.kind] += receive
            except KeyError:
                self.resources[receive.kind] = copy.copy(receive)
            try:
                target.resources[receive.kind] -= receive
            except KeyError:
                target.resources[receive.kind] = Resource(receive.kind, 0)
                target.resources[receive.kind] -= receive
    def accept(self, source, give, receive):
        """Decide whether to accept or reject an offer"""
        #go through AI to make decision, update AI here
        #for now just make a random choice
        return bool(random.randrange(2))
    def take_turn(self):
        """Take a turn in the Game"""
        print("{0} abides.".format(self.name))
