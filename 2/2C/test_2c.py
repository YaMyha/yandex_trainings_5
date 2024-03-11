import unittest
from unittest.mock import patch
from io import StringIO
from task_2c import c


class Task2ATest(unittest.TestCase):
    @patch('builtins.input', side_effect=['4', '1 5 2 1'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_1(self, mock_stdout, mock_input):
        c()
        self.assertEqual(mock_stdout.getvalue().strip(), '1')

    @patch('builtins.input', side_effect=['4', '5 12 4 3'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_2(self, mock_stdout, mock_input):
        c()
        self.assertEqual(mock_stdout.getvalue().strip(), '24')

    @patch('builtins.input', side_effect=['2', '1 1'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_3(self, mock_stdout, mock_input):
        c()
        self.assertEqual(mock_stdout.getvalue().strip(), '2')

    @patch('builtins.input', side_effect=['2', '1000 1'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_4(self, mock_stdout, mock_input):
        c()
        self.assertEqual(mock_stdout.getvalue().strip(), '999')