# funny solution with recursive approach, but defective on big numbers
def e():
    global result_size, k
    inp = input().split()
    n = inp[0]
    k, d = map(int, inp[1:3])
    result_size = len(n) + d

    answer = recursive_execution(n)
    if answer:
        print(answer[0])
    else:
        print("-1")


def recursive_execution(income):
    global result_size, k
    if len(income) == result_size:
        return income

    divisible_numbers = []
    result = []
    for number in range(10):
        current_income = income + str(number)
        if int(current_income) % k == 0:
            divisible_numbers.append(current_income)
    for num in divisible_numbers:
        returned_value = recursive_execution(num)
        if returned_value:
            if isinstance(returned_value, list):
                result.extend(returned_value)
            else:
                result.append(returned_value)
    return result

# e()