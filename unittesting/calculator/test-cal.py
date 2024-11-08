import unittest
from calculator.cal import Calculator


class TestCal(unittest.TestCase):
    def testAdd(self):
        calculator = Calculator()
        self.assertEqual(calculator.add(10, 5), 15)
        self.assertEqual(calculator.add(-1, 1), 0)
        self.assertEqual(calculator.add(-5, 3), -2)

    def testSubtract(self):
        calculator = Calculator()
        self.assertEqual(calculator.subtract(10, 5), 5)
        self.assertEqual(calculator.subtract(-1, 1), -2)
        self.assertEqual(calculator.subtract(-5, 3), -8)

    def testMultiply(self):
        calculator = Calculator()
        self.assertEqual(calculator.multiply(10, 5), 50)
        self.assertEqual(calculator.multiply(-1, 1), -1)
        self.assertEqual(calculator.multiply(-5, 3), -15)

    def testDivide(self):
        calculator = Calculator()
        self.assertEqual(calculator.divide(10, 5), 2)
        self.assertEqual(calculator.divide(20, 5), 4)
        self.assertEqual(calculator.divide(15, 5), 3)

        with self.assertRaises(ValueError):
            calculator.divide(20, 0)


if __name__ == "__main__":
    unittest.main()
