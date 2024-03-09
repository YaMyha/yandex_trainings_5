import unittest
from unittest.mock import patch
from io import StringIO
from D.task_d import d
# from task_d_updated import process_chess_field as d


class TaskCTest(unittest.TestCase):
    @patch('builtins.input', side_effect=['********', '********', '*R******', '********', '********', '********', '********', '********'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_1(self, mock_stdout, mock_input):
        d()
        self.assertEqual(mock_stdout.getvalue().strip(), '49')

    @patch('builtins.input', side_effect=['********', '********', '******1B*', '********', '********', '********', '********', '********'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_2(self, mock_stdout, mock_input):
        d()
        self.assertEqual(mock_stdout.getvalue().strip(), '54')

    @patch('builtins.input',
           side_effect=['********', '*R******', '********', '*****1B**', '********', '********', '********', '********'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_3(self, mock_stdout, mock_input):
        d()
        self.assertEqual(mock_stdout.getvalue().strip(), '40')

    @patch('builtins.input',
           side_effect=['BBRRRBRB', 'RBRBRBRB', 'RRRRRRRR', 'BBBBBBBB', 'RBRRRRRR', 'BBBRRRBB', 'BBBBBBBB', 'BBBBBBBB'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_5(self, mock_stdout, mock_input):
        d()
        self.assertEqual(mock_stdout.getvalue().strip(), '0')

    @patch('builtins.input',
           side_effect=['********', '*1B******', 'BRB*****', '*1B******', '********', '********', '********', '********'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_dunno(self, mock_stdout, mock_input):
        d()
        self.assertEqual(mock_stdout.getvalue().strip(), '45')

    @patch('builtins.input',
           side_effect=['BBBBBBB*', '******R*', '*****R**', '****R***', '***R****', '**R*****', '*R******', 'R*******'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_9(self, mock_stdout, mock_input):
        d()
        self.assertEqual(mock_stdout.getvalue().strip(), '1')

    @patch('builtins.input',
           side_effect=['1B*******', '********', '********', '********', '********', '********', '********', '********'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_b_left_high_corner(self, mock_stdout, mock_input):
        d()
        self.assertEqual(mock_stdout.getvalue().strip(), '56')

    @patch('builtins.input',
           side_effect=['*******1B', '********', '********', '********', '********', '********', '********', '********'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_b_right_high_corner(self, mock_stdout, mock_input):
        d()
        self.assertEqual(mock_stdout.getvalue().strip(), '56')

    @patch('builtins.input',
           side_effect=['********', '********', '********', '********', '********', '********', '********', '1B*******'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_b_left_down_corner(self, mock_stdout, mock_input):
        d()
        self.assertEqual(mock_stdout.getvalue().strip(), '56')

    @patch('builtins.input',
           side_effect=['********', '********', '********', '********', '********', '********', '********', '*******1B'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_b_right_high_corner(self, mock_stdout, mock_input):
        d()
        self.assertEqual(mock_stdout.getvalue().strip(), '56')

    @patch('builtins.input',
           side_effect=['R*******', '********', '********', '********', '********', '********', '********', '********'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_r_left_high_corner(self, mock_stdout, mock_input):
        d()
        self.assertEqual(mock_stdout.getvalue().strip(), '49')

    @patch('builtins.input',
           side_effect=['*******R', '********', '********', '********', '********', '********', '********', '********'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_r_right_high_corner(self, mock_stdout, mock_input):
        d()
        self.assertEqual(mock_stdout.getvalue().strip(), '49')

    @patch('builtins.input',
           side_effect=['********', '********', '********', '********', '********', '********', '********', 'R*******'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_r_left_down_corner(self, mock_stdout, mock_input):
        d()
        self.assertEqual(mock_stdout.getvalue().strip(), '49')

    @patch('builtins.input',
           side_effect=['********', '********', '********', '********', '********', '********', '********', '*******R'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_r_right_high_corner(self, mock_stdout, mock_input):
        d()
        self.assertEqual(mock_stdout.getvalue().strip(), '49')

