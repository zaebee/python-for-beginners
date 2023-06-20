"""Tests for Day_5 tasks."""
from . import tasks
import unittest


class TasksTest(unittest.TestCase):

  def test_square_odds(self):
    actual = tasks.square_odds('1,2,3,4,5,6,7,8,9')

    expected = '1,9,25,49,81'
    self.assertEqual(actual, expected)

  def test_transactions(self):
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
