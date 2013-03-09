#!/usr/bin/env python
"""Unit tests for the Resource class"""

from unittest import TestCase
from esotera.resource import Resource 

class TestEvent(TestCase):
    
    def test_creation(self):
        resource = Resource('food',10)
        self.assertEqual(resource.kind,'food')
        self.assertEqual(resource.quantity, 10)
    
    def test_addition(self):
        res1 = Resource('food',1)
        res2 = Resource('food',1)
        sum = res1 + res2
        self.assertEqual(sum.quantity, 2)
    
    def test_iaddition(self):
        res1 = Resource('food',1)
        res2 = Resource('food',1)
        res1 += res2
        self.assertEqual(res1.quantity, 2)
    
    def test_numeric_addition(self):
        res1 = Resource('food',1)
        sum = res1 + 1
        self.assertEqual(sum.quantity, 2)
    
    def test_numeric_iaddition(self):
        res1 = Resource('food',1)
        res1 += 1
        self.assertEqual(res1.quantity, 2)
    
    def test_subtraction(self):
        res1 = Resource('food',1)
        res2 = Resource('food',1)
        sum = res1 - res2
        self.assertEqual(sum.quantity, 0)
    
    def test_isubtraction(self):
        res1 = Resource('food',1)
        res2 = Resource('food',1)
        res1 -= res2
        self.assertEqual(res1.quantity, 0)
    
    def test_numeric_subtraction(self):
        res1 = Resource('food',1)
        sum = res1 - 1
        self.assertEqual(sum.quantity, 0)
    
    def test_numeric_isubtraction(self):
        res1 = Resource('food',1)
        res1 -= 1
        self.assertEqual(res1.quantity, 0)
    
    def test_multiplication(self):
        res1 = Resource('food',1)
        res2 = Resource('food',1)
        result = res1 * res2
        self.assertEqual(result.quantity, 1)
    
    def test_numeric_multiplication(self):
        res1 = Resource('food',1)
        result = res1 * 2
        self.assertEqual(result.quantity, 2)
    
    def test_floordivision(self):
        res1 = Resource('food',1)
        res2 = Resource('food',2)
        sum = res1 // res2
        self.assertEqual(sum.quantity, 0)
    
    def test_numeric_floordivision(self):
        res1 = Resource('food',1)
        sum = res1 // 2
        self.assertEqual(sum.quantity, 0)
    
    def test_add_type_incompatibility(self):
        res1 = Resource('food',1)
        res2 = Resource('mate',1)
        with self.assertRaises(TypeError):
            res1 + res2
    
    def test_iadd_type_incompatibility(self):
        res1 = Resource('food',1)
        res2 = Resource('mate',1)
        with self.assertRaises(TypeError):
            res1 += res2
    
    def test_sub_type_incompatibility(self):
        res1 = Resource('food',1)
        res2 = Resource('mate',1)
        with self.assertRaises(TypeError):
            res1 - res2
    
    def test_isub_type_incompatibility(self):
        res1 = Resource('food',1)
        res2 = Resource('mate',1)
        with self.assertRaises(TypeError):
            res1 -= res2
    
    def test_mul_type_incompatibility(self):
        res1 = Resource('food',1)
        res2 = Resource('mate',1)
        with self.assertRaises(TypeError):
            res1 * res2

    def test_floordiv_type_incompatibility(self):
        res1 = Resource('food',1)
        res2 = Resource('mate',1)
        with self.assertRaises(TypeError):
            res1 // res2

    def test_hashable(self):
        res1 = Resource('dead parrot', 1)
        res2 = Resource('dead parrot', 2)
        res3 = Resource('live parrot', 1)

        test_dict = {res1: res1 }
        self.assertIn(res1, test_dict)
        self.assertIn(res2, test_dict)
        self.assertNotIn(res3, test_dict)

    def test_eq(self):
        res1 = Resource('dead parrot', 1)
        res2 = Resource('dead parrot', 2)
        res3 = Resource('live parrot', 1)

        self.assertTrue(res1 == res2)
        self.assertFalse(res1 == res3)

    def test_ne(self):
        res1 = Resource('dead parrot', 1)
        res2 = Resource('dead parrot', 2)
        res3 = Resource('live parrot', 1)

        self.assertFalse(res1 != res2)
        self.assertTrue(res1 != res3)

