#!/usr/bin/env python
"""Unit tests for the Actor class"""

from unittest import TestCase
from mock import Mock
from esotera.actor import Actor 
from esotera.resource import Resource

class TestEvent(TestCase):
    def setUp(self):
        self.actor1 = Actor()
        self.actor2 = Actor('Cleese')
        self.food = Resource('food', 5)
        self.money = Resource('money', 25)

        resources = {self.food : self.food}
        wants = {self.money : self.money}
        needs = {self.food : self.food}
        self.actor3 = Actor('Cleese', resources, needs, wants)
    def test_creation_with_no_name(self):
        self.assertNotEqual(self.actor1.name, None)
        self.assertFalse(self.actor1.resources)
        self.assertFalse(self.actor1.needs)
        self.assertFalse(self.actor1.wants)
    def test_creation_with_name(self):
        self.assertEqual(self.actor2.name, 'Cleese')
        self.assertFalse(self.actor2.resources)
        self.assertFalse(self.actor2.needs)
        self.assertFalse(self.actor2.wants)
    def test_creation_with_name_and_resources(self):
        resources = {self.food : self.food}
        actor = Actor('Cleese', resources)
        self.assertDictEqual(actor.resources, resources)
        self.assertFalse(actor.needs)
        self.assertFalse(actor.wants)
    def test_creation_with_name_and_all_resources(self):
        resources = {self.food : self.food}
        wants = {self.money : self.money}
        needs = {self.food : self.food}
        actor = Actor('Cleese', resources, needs, wants)
        self.assertDictEqual(actor.resources, resources)
        self.assertDictEqual(actor.needs, needs)
        self.assertDictEqual(actor.wants, wants)
    def test_offer_accept(self):
        acceptor = Actor('YesMan')
        acceptor.accept = Mock(return_value=True)
        self.actor1.offer(target = acceptor, give = self.money, receive = self.food) 
        self.assertEqual(self.actor1.resources[self.money].quantity, -25)
        self.assertEqual(self.actor1.resources[self.food].quantity, 5)
        self.assertEqual(acceptor.resources[self.money].quantity, 25)
        self.assertEqual(acceptor.resources[self.food].quantity, -5)
    def test_exchange(self):
        self.actor1.exchange(target = self.actor2, receive = self.money, give = self.food)
        self.assertEqual(self.actor1.resources[self.money].quantity, 25)
        self.assertEqual(self.actor1.resources[self.food].quantity, -5)
        self.assertEqual(self.actor2.resources[self.money].quantity, -25)
        self.assertEqual(self.actor2.resources[self.food].quantity, 5)
    def test_gift(self):
        self.actor1.exchange(target = self.actor2, receive = None, give = self.food)
        self.assertEqual(self.actor1.resources[self.food].quantity, -5)
        self.assertEqual(self.actor2.resources[self.food].quantity, 5)
        with self.assertRaises(KeyError):
            self.actor1.resources[self.money].quantity
    def test_take(self):
        self.actor1.exchange(target = self.actor2, receive = self.money, give = None)
        self.assertEqual(self.actor1.resources[self.money].quantity, 25)
        self.assertEqual(self.actor2.resources[self.money].quantity, -25)
        with self.assertRaises(KeyError):
            self.actor1.resources[self.food].quantity = 1
    def test_accept(self):
        #not sure of an appropriate test here since it will ultimately be probabilistic
        #just check you get true or false
        ret = self.actor2.accept(source = self.actor1, receive = self.money, give = self.food)
        self.assertIn(ret, [True, False])
    def test_available_resources(self):
        expected = [ self.food ]
        self.assertListEqual(self.actor3.available_resources(), expected)
    def test_desired_resources(self):
        expected = [ self.food, self.money ]
        self.assertListEqual(self.actor3.desired_resources(), expected)

        
