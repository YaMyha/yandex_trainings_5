def load_test_data():
    file_path = '33.txt'

    try:
        with open(file_path, 'r') as file:
            data = [line.strip() for line in file]

        n = int(data[0])
        berries = [line for line in data[1:]]
        return n, berries
    except FileNotFoundError:
        print(f"Файл по пути '{file_path}' не найден.")
    except Exception as e:
        print(f"Произошла ошибка при чтении файла: {e}")


def save_test_answer(answer, order):
    file_path = '33a.txt'

    try:
        with open(file_path, 'w') as file:
            file.write(str(answer) + '\n')
            file.write(order)
    except FileNotFoundError:
        print(f"Файл по пути '{file_path}' не найден.")
    except Exception as e:
        print(f"Произошла ошибка при чтении файла: {e}")


def e2_test():
    n, berries = load_test_data()
    berries_origin = list(enumerate([list(map(int, berry.split())) for berry in berries], start=1))
    berries_order_last_part = []
    berries_order_beginning = []
    result = 0
    max_result = 0
    max_up, max_up_i = -1, -1  # maximum up in list where up <= down and appropriate index
    max_down, max_down_up, max_down_i = -1, -1, -1  # maximum down in list where up > down, appropriate up and index

    for i, pair in berries_origin:
        up = pair[0]
        down = pair[1]

        if down < up:
            if down > max_down:
                if max_down_i != -1:
                    result += max_down_up
                    if max_result < result:
                        max_result = result
                    result -= max_down
                    berries_order_beginning.append(max_down_i)
                max_down, max_down_up, max_down_i = down, up, i
            else:
                result += up
                if max_result < result:
                    max_result = result
                result -= down
                berries_order_beginning.append(i)
        else:
            if up > max_up:
                if max_up_i != -1:
                    berries_order_last_part.append(max_up_i)
                max_up, max_up_i = up, i
            else:
                berries_order_last_part.append(i)

    berries_origin = None
    berries_order = []
    # if we've found equal up-downs or where down bigger than up
    if max_up_i != -1:
        berries_order.extend(berries_order_beginning)
        if max_down_i != -1:
            berries_order.extend([max_down_i, max_up_i])
            result = max(result + max_down_up, result + max_down_up - max_down + max_up)
        else:
            result = max(result, result + max_up)
            berries_order.extend([max_up_i])
        berries_order.extend(berries_order_last_part)
    else:
        berries_order.extend(berries_order_beginning)
        berries_order.append(max_down_i)
        result += max_down_up

    save_test_answer(result, ' '.join(list(map(str, berries_order))))
    print(result)
    print(*berries_order)


def e2():
    n = int(input())
    berries_origin = list(enumerate([list(map(int, input().split())) for _ in range(n)], start=1))
    berries_order_last_part = []
    berries_order_beginning = []
    result = 0
    max_result = 0
    max_up, max_up_i = -1, -1  # maximum up in list where up <= down and appropriate index
    max_down, max_down_up, max_down_i = -1, -1, -1  # maximum down in list where up > down, appropriate up and index

    for i, pair in berries_origin:
        up = pair[0]
        down = pair[1]

        if down < up:
            if down > max_down:
                if max_down_i != -1:
                    result += max_down_up
                    if max_result < result:
                        max_result = result
                    result -= max_down
                    berries_order_beginning.append(max_down_i)
                max_down, max_down_up, max_down_i = down, up, i
            else:
                result += up
                if max_result < result:
                    max_result = result
                result -= down
                berries_order_beginning.append(i)
        else:
            if up > max_up:
                if max_up_i != -1:
                    berries_order_last_part.append(max_up_i)
                max_up, max_up_i = up, i
            else:
                berries_order_last_part.append(i)

    berries_origin = None
    berries_order = []
    # if we've found equal up-downs or where down bigger than up
    if max_up_i != -1:
        berries_order.extend(berries_order_beginning)
        if max_down_i != -1:
            berries_order.extend([max_down_i, max_up_i])
            result = max(result + max_down_up, result + max_down_up - max_down + max_up)
        else:
            result = max(result, result + max_up)
            berries_order.extend([max_up_i])
        berries_order.extend(berries_order_last_part)
    else:
        berries_order.extend(berries_order_beginning)
        berries_order.append(max_down_i)
        result += max_down_up

    print(result)
    print(*berries_order)


if __name__ == "__main__":
    e2_test()
    # e2()
