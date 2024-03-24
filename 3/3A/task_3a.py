def a():
    n = int(input())

    input()
    result = set(input().split())

    for i in range(n-1):
        input()
        result = result & set(input().split())

    result = sorted(result)
    print(len(result))
    print(*result)
a()
