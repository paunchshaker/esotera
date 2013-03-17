"""This module contains code for a generic Actor class"""
import random
import copy
from esotera.resource import Resource

class Actor:
    """The actor class is the base class for entities that can perform actions.
    They are not necessarily organic (i.e. they might represent political,
    religious or social bodies)."""
    
    #class variables 
    number = 0

    def __init__(self, name = None, resources = dict(), 
                 needs = dict(), wants = dict()):
        """Initialize a new Actor."""
        if name:
            self.name = name
        else:
            Actor.number += 1
            #set the default name to just be the number of the actor created
            self.name = "Actor" + str(Actor.number)
        #the following are resources the Actor has in its possession    
        self.resources = dict(resources)
        #the following are resources essential to the continued 
        #existence of the Actor
        self.needs = dict(needs)
        #the following are resources the Actor desires, but does not need
        self.wants = dict(wants)
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
                self.resources[give] -= give
            except KeyError:
                self.resources[give] = copy.copy(give)
                self.resources[give].quantity = 0
                self.resources[give] -= give
            try:
                target.resources[give] += give
            except KeyError:
                target.resources[give] = copy.copy(give)
        else:
            give = "nothing"
        if receive:
            try:
                self.resources[receive] += receive
            except KeyError:
                self.resources[receive] = copy.copy(receive)
            try:
                target.resources[receive] -= receive
            except KeyError:
                target.resources[receive] = Resource(receive.kind, 0)
                target.resources[receive] -= receive
        else:
            receive = "nothing"
        exchange_text = "{0} gave {1} {2} in exchange for {3}."
        print( exchange_text.format(self.name, target.name, give, receive))
    def accept(self, source, give, receive):
        """Decide whether to accept or reject an offer"""
        #go through AI to make decision, update AI here
        #for now just make a random choice
        return random.choice( [True, False] )
    def available_resources(self):
        """Return a list of the available (non-zero) resources for exchange"""
        available = [ res for res in self.resources.values()
                      if res.quantity > 0 ]
        return available
    def desired_resources(self):
        """Return a (ranked) list of the resources the Actor desires"""
        desired = [ res for res in self.needs.values() if res.quantity > 0 ] 
        desired.extend([ res for res in self.wants.values()
                         if res.quantity > 0 ])
        return desired
    def take_turn(self, actors):
        """Take a turn in the Game"""
        
        #pick an actor at random
        available_actors = [ act for act in actors if act is not self]
        actor = random.choice(available_actors)
        
        #make an offer at random
        to_give = None
        if self.available_resources():
            res_to_give = random.choice(self.available_resources())
            amount_to_give = 1
            if res_to_give.quantity > 1:
                amount_to_give = random.randrange(1, res_to_give.quantity)
            to_give = Resource( kind = res_to_give.kind, 
                                quantity = amount_to_give )

        to_take = None
        if actor.available_resources():
            res_to_take = random.choice(actor.available_resources())
            amount_to_take = 1
            if res_to_take.quantity > 1:
                amount_to_take = random.randrange(1, res_to_take.quantity)
            to_take = Resource( kind = res_to_take.kind, 
                                quantity = amount_to_take )
        
        if to_give or to_take:
            self.offer( target = actor, give = to_give, receive = to_take)
        else:
            print("{0} abides.".format(self.name))
    def __str__(self):
        resources_had = [ str(res) for res in self.resources.values() ]
        return "{0} (has {1})".format( self.name, ", ".join( resources_had ) )
