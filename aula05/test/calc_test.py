import unittest
from utils.is_even import is_even

class UtilsTest(unittest.TestCase):
    
    def test_must_return_correct_values_for_even_numbers(self):
        self.assertTrue(is_even(10))
        self.assertFalse(is_even(1))

