import unittest
from unittest.mock import patch
from io import StringIO
from task_3a import a

class Task3ATest(unittest.TestCase):
    @patch('builtins.input', side_effect=['1', '2', 'GoGetIt Life'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_1(self, mock_stdout, mock_input):
        a()
        self.assertEqual(mock_stdout.getvalue().strip(), '2\nGoGetIt Life')

    @patch('builtins.input', side_effect=['2', '2', 'Love Life', '2', 'Life GoodDay'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_2(self, mock_stdout, mock_input):
        a()
        self.assertEqual(mock_stdout.getvalue().strip(), '1\nLife')

    @patch('builtins.input', side_effect=['1', '1', 'GoGetIt'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_3(self, mock_stdout, mock_input):
        a()
        self.assertEqual(mock_stdout.getvalue().strip(), '1\nGoGetIt')

    @patch('builtins.input', side_effect=['10', '1', 'a', '1', 'b', '1', 'c', '1', 'd', '1', 'e', '1', 'f',
                                          '1', 'g', '1', 'h', '1', 'i', '1', 'j'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_4(self, mock_stdout, mock_input):
        a()
        self.assertEqual(mock_stdout.getvalue().strip(), '0\n')

    @patch('builtins.input', side_effect=['10', '1', 'a', '1', 'a', '1', 'a', '1', 'a', '1', 'a', '1', 'a',
                                          '1', 'a', '1', 'a', '1', 'a', '1', 'a'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_4(self, mock_stdout, mock_input):
        a()
        self.assertEqual(mock_stdout.getvalue().strip(), '1\na')