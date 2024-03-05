import unittest
from unittest.mock import patch
from io import StringIO
from task_c import c


class TaskCTest(unittest.TestCase):
    @patch('builtins.input', side_effect=['5', '1', '4', '12', '9', '0'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_default(self, mock_stdout, mock_input):
        c()
        self.assertEqual(mock_stdout.getvalue().strip(), '8')

    @patch('builtins.input', side_effect=['5', '0', '1', '2', '3', '1000000000'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_3(self, mock_stdout, mock_input):
        c()
        self.assertEqual(mock_stdout.getvalue().strip(), '250000005')
