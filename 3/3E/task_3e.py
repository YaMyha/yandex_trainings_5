def e():
    n_1, set_1 = int(input()), set(map(int, input().split()))
    n_2, set_2 = int(input()), set(map(int, input().split()))
    n_3, set_3 = int(input()), set(map(int, input().split()))

    result = set(set_1 & set_2 | set_2 & set_3 | set_1 & set_3)

    print(*sorted(list(result)))



