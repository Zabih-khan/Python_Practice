import unittest
from employee import Employee


class TestEmployee(unittest.TestCase):
    def testEmail(self):
        emp_1 = Employee("John", "Doe", 50000)
        emp_2 = Employee("Jane", "Doe", 60000)

        self.assertEqual(emp_1.email, "John.Doe@gmail.com")
        self.assertEqual(emp_2.email, "Jane.Doe@gmail.com")

        emp_1.first = "Jim"
        emp_2.first = "Jame"
        self.assertEqual(emp_1.email, "Jim.Doe@gmail.com")
        self.assertEqual(emp_2.email, "Jame.Doe@gmail.com")


if __name__ == "__main__":
    unittest.main()
