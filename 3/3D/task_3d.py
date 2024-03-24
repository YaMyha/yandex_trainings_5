def d():
    n, k = map(int, input().split())
    seq = list(map(int, input().split()))

    positions = {}

    for i, num in enumerate(seq):
        if num in positions.keys() and i - positions[num] <= k:
            print('YES')
            break
        else:
            positions[num] = i
    else:
        print('NO')
