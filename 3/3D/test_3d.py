import unittest
from unittest.mock import patch
from io import StringIO
from task_3d import d


class Task3DTest(unittest.TestCase):
    @patch('builtins.input', side_effect=['4 2', '1 2 3 1'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_1(self, mock_stdout, mock_input):
        d()
        self.assertEqual(mock_stdout.getvalue().strip(), 'NO')

    @patch('builtins.input', side_effect=['4 1', '1 0 1 1'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_2(self, mock_stdout, mock_input):
        d()
        self.assertEqual(mock_stdout.getvalue().strip(), 'YES')

    @patch('builtins.input', side_effect=['6 2', '1 2 3 1 2 3'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_3(self, mock_stdout, mock_input):
        d()
        self.assertEqual(mock_stdout.getvalue().strip(), 'NO')

    @patch('builtins.input', side_effect=['1 1', '1'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_4(self, mock_stdout, mock_input):
        d()
        self.assertEqual(mock_stdout.getvalue().strip(), 'NO')

    @patch('builtins.input', side_effect=['2 1', '1 1'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_5(self, mock_stdout, mock_input):
        d()
        self.assertEqual(mock_stdout.getvalue().strip(), 'YES')

    @patch('builtins.input', side_effect=['2 2', '1 1'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_6(self, mock_stdout, mock_input):
        d()
        self.assertEqual(mock_stdout.getvalue().strip(), 'YES')