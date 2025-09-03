import unittest

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = calculator

    def tearDown(self):
        pass

    def test_addition(self):
        result = self.calculator(2.5, 3)
        self.assertEqual(result['addition'], 5.5)

    def test_subtraction(self):
        result = self.calculator(5, -3)
        self.assertEqual(result['subtraction'], 2)

    def test_multiplication(self):
        result = self.calculator(4, 7)
        self.assertEqual(result['multiplication'], 28)

    def test_division(self):
        result = self.calculator(10, 2)
        self.assertEqual(result['division'], 5.0)

    def test_zero_division(self):
        with self.assertRaises(ZeroDivisionError):
            self.calculator(3, 0)

    def test_type_error(self):
        with self.assertRaises(ValueError):
            self.calculator(2.5, "3")

    def test_one_non_float(self):
        with self.assertRaises(ValueError):
            self.calculator("2.5", 3)