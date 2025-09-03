import math
import unittest

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = calculator

    def tearDown(self):
        pass

    def test_valid_numbers(self):
        a = 10.5
        b = 2.3
        result_add, result_sub, result_mul, result_div = self.calculator(a, b)
        expected_add, expected_sub, expected_mul, expected_div = (12.8, -8.2, 24.65, 4.565551275460683)
        self.assertAlmostEqual(result_add, expected_add)
        self.assertAlmostEqual(result_sub, expected_sub)
        self.assertAlmostEqual(result_mul, expected_mul)
        self.assertAlmostEqual(result_div, expected_div)

    def test_zero_division(self):
        a = 10.5
        b = 0.0
        with self.assertRaises(ZeroDivisionError):
            _ = self.calculator(a, b)

    def test_negative_numbers(self):
        a = -10.5
        b = -2.3
        result_add, result_sub, result_mul, result_div = self.calculator(a, b)
        expected_add, expected_sub, expected_mul, expected_div = (22.8, 12.8, -246.5, -4.565551275460683)
        self.assertAlmostEqual(result_add, expected_add)
        self.assertAlmostEqual(result_sub, expected_sub)
        self.assertAlmostEqual(result_mul, expected_mul)
        self.assertAlmostEqual(result_div, expected_div)

    def test_invalid_input_types(self):
        a = "10.5"
        with self.assertRaises(TypeError):
            _ = self.calculator(a, 2.3)
        b = [1, 2, 3]
        with self.assertRaises(TypeError):
            _ = self.calculator(10.5, b)