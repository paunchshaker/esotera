"""This module contains code for a generic actor ai"""

import random
from esotera.resource import Resource
from esotera.game_object import GameObject

class Intellect(GameObject):
    """The Intellect class is the base class for artificial intelligence
    controlling Actors. Its purpose is to observe the state of the world,
    the actor, its relationships and make decisions."""

    def __init__(self, actor):
        self.actor = actor
        actor.intellect = self

    def accept(self, source, give, receive):
        return random.choice( [True, False] )

    def take_turn(self):
        """Take a turn in the Game"""
        
        #pick an actor at random
        actors = self.game.actors
        available_actors = [ act for act in actors if act is not self.actor]
        actor = random.choice(available_actors)
        
        #make an offer at random
        to_give = None
        if self.actor.available_resources():
            res_to_give = random.choice(self.actor.available_resources())
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
            self.actor.offer( target = actor, give = to_give, receive = to_take)
        else:
            print("{0} abides.".format(self.actor.name))
