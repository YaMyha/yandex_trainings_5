import unittest
from unittest.mock import patch
from io import StringIO
from task_3c import c


class Task3CTest(unittest.TestCase):
    @patch('builtins.input', side_effect=['5', '1 2 3 4 5'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_1(self, mock_stdout, mock_input):
        c()
        self.assertEqual(mock_stdout.getvalue().strip(), '3')

    @patch('builtins.input', side_effect=['10', '1 1 2 3 5 5 2 2 1 5'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_2(self, mock_stdout, mock_input):
        c()
        self.assertEqual(mock_stdout.getvalue().strip(), '4')

    @patch('builtins.input', side_effect=['10', '1 1 2 3 5 5 2 2 1 5'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_2(self, mock_stdout, mock_input):
        c()
        self.assertEqual(mock_stdout.getvalue().strip(), '4')

    @patch('builtins.input', side_effect=['1', '1'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_3(self, mock_stdout, mock_input):
        c()
        self.assertEqual(mock_stdout.getvalue().strip(), '0')

    @patch('builtins.input', side_effect=['2', '1 1'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_4(self, mock_stdout, mock_input):
        c()
        self.assertEqual(mock_stdout.getvalue().strip(), '0')

    @patch('builtins.input', side_effect=['5', '5 4 3 2 1'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_5(self, mock_stdout, mock_input):
        c()
        self.assertEqual(mock_stdout.getvalue().strip(), '3')

    @patch('builtins.input', side_effect=['1', '0'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_6(self, mock_stdout, mock_input):
        c()
        self.assertEqual(mock_stdout.getvalue().strip(), '0')