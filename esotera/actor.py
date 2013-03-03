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
        return random.choice( [True, False] )
    def available_resources(self):
        available_resources = []
        if self.resources:
            available_resources = [ res for res in self.resources.values() if res != 0]
        return available_resources

    def take_turn(self, actors, resources):
        """Take a turn in the Game"""
        
        #pick an actor at random
        actor = random.choice( actors )
        
        #make an offer at random
        to_give = None
        if self.available_resources():
            resource_to_give = random.choice(self.available_resources())
            amount_to_give = 1
            if resource_to_give.quantity > 1:
                amount_to_give = random.randrange(1,resource_to_give.quantity)
            to_give = Resource( kind = resource_to_give.kind, quantity = amount_to_give)

        to_take = None
        if actor.available_resources():
            resource_to_take = random.choice(actor.available_resources())
            amount_to_take = 1
            if resource_to_take.quantity > 1:
                amount_to_take = random.randrange(1, resource_to_take.quantity)
            to_take = Resource( kind = resource_to_take.kind, quantity = amount_to_take)
        
        if to_give or to_take:
            self.offer( target = actor, give = to_give, receive = to_take)
        else:
            print("{0} abides.".format(self.name))
