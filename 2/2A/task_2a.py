def a():
    n = int(input())

    x_list = []
    y_list = []
    for i in range(n):
        current_point = input().split()
        x_list.append(int(current_point[0]))
        y_list.append(int(current_point[1]))

    x1, x2 = find_min_and_max(x_list)
    y1, y2 = find_min_and_max(y_list)

    print(f"{x1} {y1} {x2} {y2}")


def find_min_and_max(search_list):
    length = len(search_list)
    if length == 2:
        return min(search_list), max(search_list)

    maximums = []
    minimums = []

    for i in range(0, length, 2):
        curr_value = search_list[i]
        if i == length-1:
            maximums.append(curr_value)
            minimums.append(curr_value)
        else:
            next_value = search_list[i + 1]
            if curr_value > next_value:
                maximums.append(curr_value)
                minimums.append(next_value)
            elif curr_value < next_value:
                maximums.append(next_value)
                minimums.append(curr_value)
            else:
                maximums.append(curr_value)
                minimums.append(curr_value)

    max_value = max(maximums)
    min_value = min(minimums)

    return min_value, max_value

if __name__ == "__main__":
    a()
