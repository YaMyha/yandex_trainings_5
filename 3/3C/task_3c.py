def c():
    n = int(input())
    nums = list(map(int, input().split()))

    nums_dict = {}
    for num in nums:
        if num not in nums_dict.keys():
            nums_dict[num] = 1
        else:
            nums_dict[num] += 1

    min_counter = n

    for curr_num, value in nums_dict.items():
        counter_diff_1 = n
        counter_plus_1 = n
        counter = n - value

        if curr_num - 1 in nums_dict:
            counter_diff_1 = n - value - nums_dict[curr_num-1]
        if curr_num + 1 in nums_dict:
            counter_plus_1 = n - value - nums_dict[curr_num+1]

        if counter_diff_1 < min_counter:
            min_counter = counter_diff_1
        if counter_plus_1 < min_counter:
            min_counter = counter_plus_1
        if counter < min_counter:
            min_counter = counter

    print(min_counter)


