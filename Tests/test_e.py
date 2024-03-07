import unittest
from unittest.mock import patch
from io import StringIO
from task_e import e


class TaskCTest(unittest.TestCase):
    @patch('builtins.input', side_effect=['21 108 1'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_1(self, mock_stdout, mock_input):
        e()
        self.assertEqual(mock_stdout.getvalue().strip(), '216')

    @patch('builtins.input', side_effect=['5 12 4'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_2(self, mock_stdout, mock_input):
        e()
        self.assertEqual(mock_stdout.getvalue().strip(), '-1')

    @patch('builtins.input', side_effect=['2 1 3'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_3(self, mock_stdout, mock_input):
        e()
        self.assertEqual(mock_stdout.getvalue().strip(), '2000')

    @patch('builtins.input', side_effect=['1 1 1'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_4(self, mock_stdout, mock_input):
        e()
        self.assertEqual(mock_stdout.getvalue().strip(), '10')

    @patch('builtins.input', side_effect=['29420920 98069736 69929'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_4(self, mock_stdout, mock_input):
        e()
        self.assertEqual(mock_stdout.getvalue().strip(), '294209208'+'0'*69928)



