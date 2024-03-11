def c():
    n = int(input())
    rope_len_list = list(map(int, input().split()))

    max_len = max(rope_len_list)
    sum_other_lens = sum(rope_len_list) - max_len

    diff = max_len - sum_other_lens

    if diff > 0:
        print(diff)
    else:
        print(max_len + sum_other_lens)

if __name__ == "__main__":
    c()



