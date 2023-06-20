"""Tests for Day_6 tasks."""

import tasks
import unittest


class TasksTest(unittest.TestCase):

  def test_validation(self):
    given = 'ABd1234@1,a F1#,2w3E*,2We3345'
    actual = tasks.validation(given)

    self.assertEqual(actual, 'ABd1234@1')


  def test_sort_tuples(self):
    given = '''
    Tom,19,80
    John,20,90
    Jony,17,91
    Jony,17,93
    Json,21,85
    '''
    actual = tasks.sort_tuples(given)

    expected = [
        ('John', '20', '90'), ('Jony', '17', '91'),
        ('Jony', '17', '93'), ('Json', '21', '85'), ('Tom', '19', '80')]
    self.assertEqual(actual, expected)


if __name__ == "__main__":
  unittest.main()
