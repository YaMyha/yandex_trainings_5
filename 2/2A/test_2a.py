import unittest
from unittest.mock import patch
from io import StringIO
from task_2a import a


class Task2ATest(unittest.TestCase):
    @patch('builtins.input', side_effect=['4', '1 3', '3 1', '3 5', '6 3'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_1(self, mock_stdout, mock_input):
        a()
        self.assertEqual(mock_stdout.getvalue().strip(), '1 1 6 5')

    @patch('builtins.input', side_effect=['1', '1 1'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_2(self, mock_stdout, mock_input):
        a()
        self.assertEqual(mock_stdout.getvalue().strip(), '1 1 1 1')

    @patch('builtins.input', side_effect=['3', '1 1', '1 2', '2 2'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_3(self, mock_stdout, mock_input):
        a()
        self.assertEqual(mock_stdout.getvalue().strip(), '1 1 2 2')