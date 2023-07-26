"""unittests for Day_7."""

import unittest
from . import tasks


class TasksTest(unittest.TestCase):
  """Unit tests for tasks."""

  def test_div_by_7(self):
    """Returns numbers divisible by 7."""
    given = 7
    test_object = tasks.NumGenerator(given)
    actual = test_object.div_by_7()
    expected = [0, 7]

    self.assertEqual(actual, expected)

  def test_robot(self):
    """Returns numbers divisible by 7."""
    given = '''UP 5
    DOWN 3
    LEFT 3
    RIGHT 2
    '''

    actual = tasks.robot_moves(given)
    expected = 2

    self.assertEqual(actual, expected)


if __name__ == '__main__':
  unittest.main()
