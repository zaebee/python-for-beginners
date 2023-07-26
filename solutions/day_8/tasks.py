""" Question 22
    Write a program to compute the frequency of the words from the input.
    The output should output after sorting the key alphanumerically."""


def compute_the_frequency(input_string):
    """Compute the frequency of the words and return the ordered output."""
    # Split the input string to a list
    input_list = [i for i in input_string.split(' ')]

    # Create an empty set to store future set. Set is used to remove duplicates
    output_set = set()
    for i in input_list:
        # Count each value in a list and concatenate the result with the value itself.
        # Add concatenated string to a set
        output_set.add(i + ':' + str(input_list.count(i)))

    # Convert set to a list to sort items
    output_list = list(output_set)
    output_list.sort()
    # Convert list to string to get needed format - each item should be separated by a newline
    output_string = '\n'.join([str(i) for i in output_list])
    return output_string


""" Question 23
    Write a method which can calculate square value of number.
    Using the ** operator which can be written as n**p where means n^p"""


class MathOperations:
    """ Class for math operations"""

    def __init__(self, input_int):
        self.input_int = input_int

    def square_value(self):
        """ Return the square value of number"""
        return self.input_int ** 2


""" Question 24
    Write a program to print some Python built-in functions documents, such as abs(), int(), input() 
    (raw_input() for Python 2.x).
    And add document for your own function.
    The built-in document method is __doc__"""


def return_documentation(input_func):
    return input_func.__doc__


""" Question 25
    Define a class, which have a class parameter and have a same instance parameter.
    Hint: Define an instance parameter, need to add it in __init__ method. 
    You can init an object with construct parameter or set the value later
    """


class ClassAndInstanceParameters:
    """ Class for string operations"""
    input_string = 'replace with your string'

    # Set default value for input_string, so you can initiate an object without this parameter
    def __init__(self, input_string=input_string):
        self.input_string = input_string

    def set_value(self, new_string):
        """ Method to set a new value for input_string"""
        self.input_string = new_string
