G11, G12 = list(map(int, input().split(':')))
G21, G22 = list(map(int, input().split(':')))

field = int(input())
if G11+G21 > G12+G22:
    print(0)
else:
    min_goal = G12 + G22 - G11

    if field == 1:
        if min_goal <= G12:
            print(min_goal+1-G21)
        else:
            print(min_goal-G21)
    else:
        if G11 > G22:
            print(min_goal-G21)
        else:
            print(min_goal+1-G21)

