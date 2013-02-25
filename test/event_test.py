#!/usr/bin/env python
"""Unit tests for the Event class"""

from unittest import TestCase
from esotera.event import Event 

class TestEvent(TestCase):
    def test_creation_with_no_targets(self):
        event = Event('Test')
        self.assertEqual(event.source,'Test')
    def test_creation_with_targets(self):
        event = Event('Test',['target1','target2'])
        self.assertEqual(event.source,'Test')
        self.assertListEqual(event.targets,['target1','target2'])
    def test_str_with_no_targets(self):
        event = Event('Test')
        self.assertEqual(str(event),'Test generated a generic Event targeted at: nothing.')
    def test_str_with_multiple_targets(self):
        event = Event('Test',['target1','target2'])
        self.assertEqual(str(event),'Test generated a generic Event targeted at: target1, target2.')
