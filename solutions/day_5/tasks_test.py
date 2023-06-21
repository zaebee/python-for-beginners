"""Tests for Day_5 tasks."""

import unittest
from parameterized import parameterized

from . import tasks


class TasksTest(unittest.TestCase):
  """Tests for tasks."""

  @parameterized.expand([
      ('positive', '1,2,3,4,5,6,7,8,9', '1,9,25,49,81'),
      ('negative', '-3,-2,-1,0', '9,1'),
      ('with_spaces', '-3, 1, 5,  7,4', '9,1,25,49'),
  ])
  def test_square_odds(self, _, test_input, expected):
    """Checks square for odds numbers."""
    actual = tasks.square_odds(test_input)

    self.assertEqual(actual, expected)

  def test_transactions(self):
    """Calculates amount after all transactions."""
    data = '''
    D 300
    D 300
    W 200
    D 100
    '''
    actual = tasks.transactions(data)

    expected = 500
    self.assertEqual(actual, expected)


if __name__ == '__main__':
  unittest.main()
