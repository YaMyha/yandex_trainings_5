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


def save_test_answer(answer):
    file_path = '10 (3)a.txt'

    try:
        with open(file_path, 'w') as file:
            file.write(answer)
    except FileNotFoundError:
        print(f"Файл по пути '{file_path}' не найден.")
    except Exception as e:
        print(f"Произошла ошибка при чтении файла: {e}")



def f_for_recording(n, numbers):
    n = int(n)
    numbers = list(map(is_odd, numbers.split()))

    answer = ''.join(pickup(numbers, n))
    save_test_answer(answer)
    print(answer)


def f():
    n = int(input())
    numbers = list(map(is_odd, input().split()))

    answer = ''.join(pickup(numbers, n))
    print(answer)


def is_odd(value):
    if int(value) % 2 != 0:
        return 1
    else:
        return 0


def pickup(seq, n):
    odd_number = sum(seq)
    ops = ['+' for _ in range(n-1)]
    if odd_number % 2 == 1:
        return ops
    else:
        for i in range(n):
            if seq[i - 1] != seq[i]:
                ops[i - 1] = 'x'
                break
            else:
                ops[0] = 'x'
        return ops


# first, second = load_test_data()
# f_for_recording(first, second)
# f()
