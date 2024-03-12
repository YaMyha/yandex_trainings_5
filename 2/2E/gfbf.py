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

f, s = load_test_data()
1