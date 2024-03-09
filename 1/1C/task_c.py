def c():
    n = int(input())
    spaces = [int(input()) for _ in range(n)]

    res = 0
    for i in range(n):
        res += spaces[i] // 4 + (spaces[i] % 4 // 3) * 2 + (spaces[i] % 4 % 3)

    print(res)

#c()

