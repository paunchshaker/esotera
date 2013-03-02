#!/usr/bin/env python
"""Unit tests for the Game class"""

from unittest import TestCase
from esotera.game import Game
from collections import deque 

class TestGame(TestCase):
    def setUp(self):
        self.game = Game()
    def test_game_init(self):
        self.assertEqual(self.game.actors, [])
        self.assertEqual(self.game.resources, [])
        self.assertEqual(self.game.event_queue, deque())
    def test_new_game(self):
        self.game.new_game(number_actors = 2, number_turns = 1)
        self.assertEqual(len(self.game.actors), 2)
        self.assertEqual(self.game.turn, 1)


