"""unittests for Day_8."""

import unittest
from . import tasks


class TasksTest(unittest.TestCase):
    """Unit tests for tasks."""

    def test_compute_the_frequency(self):
        """Returns sorted frequency of the words from the input string"""
        given = '''New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.'''

        actual = tasks.compute_the_frequency(given)
        expected = '''2:2
3.:1
3?:1
New:1
Python:5
Read:1
and:1
between:1
choosing:1
or:2
to:1'''

        self.assertEqual(actual, expected)

    def test_square_value(self):
        """Returns squared values."""
        given = 11
        test_object = tasks.MathOperations(given)
        actual = test_object.square_value()
        expected = 121

        self.assertEqual(actual, expected)

    def test_return_abs_documentation(self):
        """Returns documentation for a function."""
        actual = tasks.return_documentation(abs)
        self.assertIsNotNone(actual)

    def test_return_int_documentation(self):
        """Returns documentation for a function."""
        actual = tasks.return_documentation(int)
        self.assertIsNotNone(actual)

    def test_return_input_documentation(self):
        """Returns documentation for a function."""
        actual = tasks.return_documentation(input)
        self.assertIsNotNone(actual)

    def test_return_compute_the_frequency_documentation(self):
        """Returns documentation for a function."""
        actual = tasks.return_documentation(tasks.compute_the_frequency)
        self.assertIsNotNone(actual)

    def test_class_parameters(self):
        test_object = tasks.ClassAndInstanceParameters()
        actual = test_object.input_string
        expected = 'replace with your string'
        self.assertEqual(actual, expected)

    def test_instance_parameters(self):
        test_object = tasks.ClassAndInstanceParameters('my string')
        actual = test_object.input_string
        expected = 'my string'
        self.assertEqual(actual, expected)

    def test_new_set_parameters(self):
        test_object = tasks.ClassAndInstanceParameters('my string')
        test_object.set_value('my new string')
        actual = test_object.input_string
        expected = 'my new string'
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
