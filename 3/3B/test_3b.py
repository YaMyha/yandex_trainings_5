import unittest
from unittest.mock import patch
from io import StringIO
from task_3b import b


class Task3BTest(unittest.TestCase):
    @patch('builtins.input', side_effect=['dusty', 'study'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_1(self, mock_stdout, mock_input):
        b()
        self.assertEqual(mock_stdout.getvalue().strip(), 'YES')

    @patch('builtins.input', side_effect=['rat', 'bat'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_2(self, mock_stdout, mock_input):
        b()
        self.assertEqual(mock_stdout.getvalue().strip(), 'NO')

    @patch('builtins.input', side_effect=['a', 'aa'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_3(self, mock_stdout, mock_input):
        b()
        self.assertEqual(mock_stdout.getvalue().strip(), 'NO')

    @patch('builtins.input', side_effect=['1', '1'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_4(self, mock_stdout, mock_input):
        b()
        self.assertEqual(mock_stdout.getvalue().strip(), 'YES')

    @patch('builtins.input', side_effect=['cockroach', 'cockroach'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_5(self, mock_stdout, mock_input):
        b()
        self.assertEqual(mock_stdout.getvalue().strip(), 'YES')
