def left_bin_search(l, r, check, checkparams):
    while l < r:
        m = (l + r) // 2
        if check(m, checkparams):
            r = m
        else:
            l = m + 1
    return l


def check_is_ge(index, params):
    seq, x = params
    return seq[index] >= x


def a():
    n, nums, pairs_n, pairs = int(input()), sorted(list(map(int, input().split()))), int(input()), []
    [pairs.append(list(map(int, input().split()))) for i in range(pairs_n)]
    result = []

    for pair in pairs:
        left_border = left_bin_search(0, n, check_is_ge, (nums, pair[0]))
        right_border = left_bin_search(0, n, check_is_ge, (nums, pair[1]+1)) - 1
        result.append(right_border - left_border + 1)

    print(*result)

a()
if __name__ == "__main__":
    a()