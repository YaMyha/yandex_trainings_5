def count_chars():
    chars_count = {}
    for c in input():
        if c not in chars_count.keys():
            chars_count[c] = 1
        else:
            chars_count[c] += 1
    return chars_count


def b():
    f, s = count_chars(), count_chars()
    print('YES' if f == s else 'NO')

if __name__ == "__main__":
    b()