def e():
    inp = input().split()
    n = inp[0]
    k, d = map(int, inp[1:3])
    answer = -1
    for num in range(10):
        current = n + str(num)
        if int(current) % k == 0:
            answer = current
            break
    if answer != -1:
        print(answer + '0' * (d - 1))
    else:
        print(answer)


# e()
