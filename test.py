# This program was created by Can Shi on March 20, 2019
# Assignment 4 Unit Test 19W_CST8333_350

import unittest
from assignment4 import ReadData
from author import Author


class Test(unittest.TestCase):

    def test_inheritance(self):
        """
        This test tests if a child class outputs the correct result
        after overriding a method from parent class
        """
        obj1 = ReadData.__new__(ReadData)
        obj2 = Author.__new__(Author)
        self.assertEqual(obj1.getStudentNumber(), '040806036')
        self.assertEqual(obj2.getStudentNumber(), 0)
        print("This test was done by Can Shi")


if __name__ == '__main__':
    unittest.main()
