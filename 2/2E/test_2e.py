import unittest
from unittest.mock import patch
from io import StringIO
from task_2e import e2 as e

def load_test_data():
    file_path = '33.txt'

    try:
        with open(file_path, 'r') as file:
            data = [line.strip() for line in file]

        return data
    except FileNotFoundError:
        print(f"Файл по пути '{file_path}' не найден.")
    except Exception as e:
        print(f"Произошла ошибка при чтении файла: {e}")


def load_answer_data():
    file_path = '33a.txt'

    try:
        with open(file_path, 'r') as file:
            data = file.read()
        return data
    except FileNotFoundError:
        print(f"Файл по пути '{file_path}' не найден.")
    except Exception as e:
        print(f"Произошла ошибка при чтении файла: {e}")


class Task2ATest(unittest.TestCase):
    @patch('builtins.input', side_effect=['3', '1 5', '8 2', '4 4'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_1(self, mock_stdout, mock_input):
        e()
        self.assertEqual(mock_stdout.getvalue().strip(), '10\n2 3 1')

    @patch('builtins.input', side_effect=['2', '7 6', '7 4'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_2(self, mock_stdout, mock_input):
        e()
        self.assertEqual(mock_stdout.getvalue().strip(), '10\n2 1')


    @patch('builtins.input', side_effect=['7', '160714711 449656269', '822889311 446755913', '135599877 389312924',
                                          '448565595 480845266', '561330066 605997004', '61020590 573085537', '715477619 181424399'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_3(self, mock_stdout, mock_input):
        e()
        self.assertEqual(mock_stdout.getvalue().strip(), '1471516684\n7 2 5 3 1 6 4')

    @patch('builtins.input',
           side_effect=['6', '822889311 446755913', '715477619 181424399', '61020590 573085537', '480845266 448565595',
                        '135599877 389312924', '160714711 449656269'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_4(self, mock_stdout, mock_input):
        e()
        self.assertEqual(mock_stdout.getvalue().strip(), '1391031884\n2 1 4 6 5 3')
    @patch('builtins.input',
           side_effect=load_test_data())
    @patch('sys.stdout', new_callable=StringIO)
    def test_5(self, mock_stdout, mock_input):
        e()
        self.assertEqual(mock_stdout.getvalue().strip(), load_answer_data())