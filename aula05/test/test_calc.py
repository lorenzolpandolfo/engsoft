import unittest

from utils.is_even import is_even
from utils.sum import sum
from utils.divide import divide


class UtilsTest(unittest.TestCase):

    def test_must_return_correct_values_for_even_numbers(self):
        self.assertTrue(is_even(10))
        self.assertFalse(is_even(1))

    def test_must_sum_two_numbers_correctly(self):
        self.assertEqual(sum(10, 20), 30)
        self.assertEqual(sum(-10, 20), 10)
        self.assertEqual(sum(-10, -20), -30)
        self.assertEqual(sum(-10, 0), -10)
        self.assertEqual(sum(10, 0), 10)
        self.assertEqual(sum(0, 0), 0)

    def test_must_divide_two_numbers_correctly(self):
        self.assertEqual(divide(1, 1), 1)
        self.assertEqual(divide(1, 2), 0.5)
        self.assertEqual(divide(10, 2), 5)
        self.assertAlmostEqual(divide(1, 3), 0.3333333, 7)
        self.assertEqual(divide(0, 1), 0)
        with self.assertRaises(ZeroDivisionError) as ctx:
            divide(1, 0)
            self.assertEqual(str(ctx.exception), "Operação inválida: divisão por zero.")
