import unittest
from unittest.mock import patch
from io import StringIO
from task_f_wise_approach import f


# from task_f_brute_force import f

def load_test_data():
    file_path = '10 (3).txt'

    try:
        with open(file_path, 'r') as file:
            data = [line.strip() for line in file]
            return data[0], data[1]
    except FileNotFoundError:
        print(f"Файл по пути '{file_path}' не найден.")
    except Exception as e:
        print(f"Произошла ошибка при чтении файла: {e}")
def load_test_answer():
    file_path = '10 (3)a.txt'

    try:
        with open(file_path, 'r') as file:
            return file.readline()
    except FileNotFoundError:
        print(f"Файл по пути '{file_path}' не найден.")
    except Exception as e:
        print(f"Произошла ошибка при чтении файла: {e}")


class TaskCTest(unittest.TestCase):
    f, s = load_test_data()

    @patch('builtins.input', side_effect=['3', '5 7 2'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_1(self, mock_stdout, mock_input):
        f()
        self.assertEqual(mock_stdout.getvalue().strip(), '+x')

    @patch('builtins.input', side_effect=['2', '4 -5'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_2(self, mock_stdout, mock_input):
        f()
        self.assertEqual(mock_stdout.getvalue().strip(), '+')

    @patch('builtins.input', side_effect=['4', '-432300451 509430974 -600857889 -140418957'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_3(self, mock_stdout, mock_input):
        f()
        self.assertEqual(mock_stdout.getvalue().strip(), '+++')

    @patch('builtins.input', side_effect=['4', '-1 -1 -1 -1'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_13(self, mock_stdout, mock_input):
        f()
        self.assertEqual(mock_stdout.getvalue().strip(), 'x++')

    @patch('builtins.input', side_effect=[f, s])
    @patch('sys.stdout', new_callable=StringIO)
    def test_reload(self, mock_stdout, mock_input):
        f()
        self.assertEqual(mock_stdout.getvalue().strip(), load_test_answer())
