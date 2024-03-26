import unittest
from unittest.mock import patch
from io import StringIO
from task_4a import a


class Task4ATest(unittest.TestCase):
    @patch('builtins.input', side_effect=['5', '10 1 10 3 4', '4', '1 10', '2 9', '3 4', '2 2'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_1(self, mock_stdout, mock_input):
        a()
        self.assertEqual(mock_stdout.getvalue().strip(), '5 2 2 0')

    @patch('builtins.input', side_effect=['1', '1', '1', '1 1'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_2(self, mock_stdout, mock_input):
        a()
        self.assertEqual(mock_stdout.getvalue().strip(), '1')