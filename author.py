# This program was created by Can Shi on March 20, 2019
# Assignment 4 19W_CST8333_350


class Author(object):

    """
    This class will be inherited by the ReadData class in the assignment4.py file
    """
    def __init__(self, first, last):
        self.firstname = first
        self.lastname = last

    """
    This method concat first and last name and return as a string
    """
    def name(self):
        return self.firstname + " " + self.lastname

    """
    This method is to be overriden in the child class
    """
    def getStudentNumber(self):
        return 0
