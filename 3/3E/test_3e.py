import unittest
from unittest.mock import patch
from io import StringIO
from task_3e import e


class Task3ETest(unittest.TestCase):
    @patch('builtins.input', side_effect=['2', '3 1', '2', '1 3', '2', '1 2'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_1(self, mock_stdout, mock_input):
        e()
        self.assertEqual(mock_stdout.getvalue().strip(), '1 3')

    @patch('builtins.input', side_effect=['3', '1 2 2', '3', '3 4 3', '1', '5'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_2(self, mock_stdout, mock_input):
        e()
        self.assertEqual(mock_stdout.getvalue().strip(), '')

    @patch('builtins.input', side_effect=['1', '1', '1', '2', '3', '3'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_3(self, mock_stdout, mock_input):
        e()
        self.assertEqual(mock_stdout.getvalue().strip(), '')

    @patch('builtins.input', side_effect=['3', '1 2 3', '3', '1 2 3', '3', '1 2 3'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_4(self, mock_stdout, mock_input):
        e()
        self.assertEqual(mock_stdout.getvalue().strip(), '1 2 3')

    @patch('builtins.input', side_effect=['3', '1 1 1', '3', '1 1 1', '2', '1 1'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_5(self, mock_stdout, mock_input):
        e()
        self.assertEqual(mock_stdout.getvalue().strip(), '1')

    @patch('builtins.input', side_effect=['10', '14 1 7 16 1 8 5 13 17 3', '5', '19 17 11 2 9',
                                          '6', '9 18 3 1 9 14'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_6(self, mock_stdout, mock_input):
        e()
        self.assertEqual(mock_stdout.getvalue().strip(), '1 3 9 14 17')

