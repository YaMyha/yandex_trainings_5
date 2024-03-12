import unittest
from unittest.mock import patch
from io import StringIO
from task_2d import d


class Task2ATest(unittest.TestCase):
    @patch('builtins.input', side_effect=['3', '1 1', '2 1', '1 2'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_1(self, mock_stdout, mock_input):
        d()
        self.assertEqual(mock_stdout.getvalue().strip(), '8')

    @patch('builtins.input', side_effect=['1', '1 1'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_2(self, mock_stdout, mock_input):
        d()
        self.assertEqual(mock_stdout.getvalue().strip(), '4')

    @patch('builtins.input', side_effect=['64', '1 1', '1 2', '1 3', '1 4', '1 5', '1 6', '1 7', '1 8',
                                          '2 1', '2 2', '2 3', '2 4', '2 5', '2 6', '2 7', '2 8',
                                          '3 1', '3 2', '3 3', '3 4', '3 5', '3 6', '3 7', '3 8',
                                          '4 1', '4 2', '4 3', '4 4', '4 5', '4 6', '4 7', '4 8',
                                          '5 1', '5 2', '5 3', '5 4', '5 5', '5 6', '5 7', '5 8',
                                          '6 1', '6 2', '6 3', '6 4', '6 5', '6 6', '6 7', '6 8',
                                          '7 1', '7 2', '7 3', '7 4', '7 5', '7 6', '7 7', '7 8',
                                          '8 1', '8 2', '8 3', '8 4', '8 5', '8 6', '8 7', '8 8'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_3(self, mock_stdout, mock_input):
        d()
        self.assertEqual(mock_stdout.getvalue().strip(), '32')