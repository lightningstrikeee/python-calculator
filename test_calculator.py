import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(5, 7), 12)
        self.assertEqual(self.calc.add(8, 3), 11)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(6, 4), 2)
        self.assertEqual(self.calc.subtract(10, 6), 4)
    
    def test_multiply(self):
        self.assertEqual(self.calc.multiply(3, 4), 12)
        self.assertEqual(self.calc.multiply(6, 7), 42)
    
    def test_divide(self):
        self.assertEqual(self.calc.divide(8, 4), 2)
        self.assertEqual(self.calc.divide(12, 3), 4)

    def test_modulo(self):
        self.assertEqual(self.calc.modulo(7, 3), 1)
        self.assertEqual(self.calc.modulo(15, 4), 3)

    # Add the following test methods to the TestCalculator class:

if __name__ == '__main__':
    unittest.main()
