# программа не проверена
def f(n, numbers):
    # n = int(input())
    # numbers = input().split()

    nums_and_ops = '+'.join(numbers)
    result_seq = brute_force(nums_and_ops, n)
    answer = []
    for char in result_seq:
        if char == '*':
            answer.append('x')
        elif char == '+':
            answer.append('+')
    print(''.join(answer))


def is_odd(seq):
    return eval(seq) % 2 != 0


def brute_force(seq, n):
    if is_odd(seq):
        return seq
    for i in range(1, 2 * n - 1, 2):
        for j in range(i, 2 * n - 1, 2):
            seq = seq[:j] + '*' + seq[j + 1:]

            if is_odd(seq):
                return seq
        seq = seq[:i] + '*' + seq[i + 1:]


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

first, second = load_test_data()
f(first, second)
