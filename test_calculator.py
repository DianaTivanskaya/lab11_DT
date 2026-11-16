import unittest
import calculator

class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calculator.add(2, 3), 5)
        self.assertEqual(calculator.add(-2, 5), 3)
        self.assertEqual(calculator.add(0, 0), 0)

    def test_subtract(self):
        self.assertEqual(calculator.subtract(5, 3), 2)
        self.assertEqual(calculator.subtract(3, 5), -2)
        self.assertEqual(calculator.subtract(0, 0), 0)

    def test_multiply(self):
        self.assertEqual(calculator.mul(3, 4), 12)
        self.assertEqual(calculator.mul(-2, 5), -10)
        self.assertEqual(calculator.mul(0, 5), 0)

    def test_divide(self):
        self.assertEqual(calculator.div(2, 10), 5)
        self.assertEqual(calculator.div(-2, 10), -5)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            calculator.div(0, 10)

        with self.assertRaises(ZeroDivisionError):
            calculator.div(0, 5)

    def test_logarithm(self):
        self.assertAlmostEqual(calculator.logarithm(2, 8), 3)
        self.assertAlmostEqual(calculator.logarithm(10, 100), 2)
        self.assertAlmostEqual(calculator.logarithm(3, 9), 2)

    def test_log_invalid_argument(self):
        with self.assertRaises(ValueError):
            calculator.logarithm(-2, 10)

        with self.assertRaises(ValueError):
            calculator.logarithm(2, -10)

    def test_log_invalid_base(self):
        with self.assertRaises(ValueError):
            calculator.logarithm(1, 10)

        with self.assertRaises(ValueError):
            calculator.logarithm(-2, 10)

        with self.assertRaises(ValueError):
            calculator.logarithm(0, 10)

    def test_hypotenuse(self):
        self.assertAlmostEqual(calculator.hypotenuse(3, 4), 5)
        self.assertAlmostEqual(calculator.hypotenuse(5, 12), 13)
        self.assertAlmostEqual(calculator.hypotenuse(8, 15), 17)

    def test_sqrt(self):
        self.assertAlmostEqual(calculator.square_root(4), 2)
        self.assertAlmostEqual(calculator.square_root(9), 3)
        self.assertAlmostEqual(calculator.square_root(25), 5)

        with self.assertRaises(ValueError):
            calculator.square_root(-4)
