import unittest
from unittest.mock import patch
from io import StringIO
from task_2b import b


class Task2ATest(unittest.TestCase):
    @patch('builtins.input', side_effect=['5 2', '1 2 3 4 5'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_1(self, mock_stdout, mock_input):
        b()
        self.assertEqual(mock_stdout.getvalue().strip(), '2')

    @patch('builtins.input', side_effect=['5 2', '5 4 3 2 1'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_2(self, mock_stdout, mock_input):
        b()
        self.assertEqual(mock_stdout.getvalue().strip(), '0')

    @patch('builtins.input', side_effect=['5 1', '5 4 3 2 1'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_3(self, mock_stdout, mock_input):
        b()
        self.assertEqual(mock_stdout.getvalue().strip(), '0')

    @patch('builtins.input', side_effect=['5 1', '1 2 10 4 10'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_4(self, mock_stdout, mock_input):
        b()
        self.assertEqual(mock_stdout.getvalue().strip(), '8')

    @patch('builtins.input', side_effect=['1 1', '1'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_5(self, mock_stdout, mock_input):
        b()
        self.assertEqual(mock_stdout.getvalue().strip(), '0')

    @patch('builtins.input', side_effect=['2 1', '1000 10'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_6(self, mock_stdout, mock_input):
        b()
        self.assertEqual(mock_stdout.getvalue().strip(), '0')

    @patch('builtins.input', side_effect=['2 1', '1000000000 1000000000'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_7(self, mock_stdout, mock_input):
        b()
        self.assertEqual(mock_stdout.getvalue().strip(), '0')