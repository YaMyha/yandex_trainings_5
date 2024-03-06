def d():
    field = []
    SIDE_LENGTH = 8
    for _ in range(SIDE_LENGTH):
        field.extend(list(input()))

    for i, cell in enumerate(field, start=0):
        if cell == 'R':
            row = i // SIDE_LENGTH
            column = i % SIDE_LENGTH
            pointer = i - 1
            while pointer != row * SIDE_LENGTH - 1:
                if field[pointer] == 'R' or field[pointer] == 'B':
                    break
                field[pointer] = 'x'
                pointer -= 1
            pointer = i + 1

            while pointer != (row + 1) * SIDE_LENGTH:
                if field[pointer] == 'R' or field[pointer] == 'B':
                    break
                field[pointer] = 'x'
                pointer += 1

            if row != 0:
                pointer = i - SIDE_LENGTH
                while True:
                    if field[pointer] == 'R' or field[pointer] == 'B':
                        break
                    field[pointer] = 'x'
                    if pointer // 8 == 0:
                        break
                    pointer -= SIDE_LENGTH

            if row != 7:
                pointer = i + SIDE_LENGTH
                while True:
                    if field[pointer] == 'R' or field[pointer] == 'B':
                        break
                    field[pointer] = 'x'
                    if pointer // 8 == 7:
                        break
                    pointer += SIDE_LENGTH
        elif cell == 'B':
            row = i // SIDE_LENGTH
            column = i % SIDE_LENGTH
            if row != 0 and column != 0:
                pointer = i - SIDE_LENGTH - 1
                while pointer >= 0:
                    if field[pointer] == 'R' or field[pointer] == 'B':
                        break
                    field[pointer] = 'x'

                    if pointer // SIDE_LENGTH == 0 or pointer % SIDE_LENGTH == 0:
                        break
                    pointer -= SIDE_LENGTH + 1

            if row != 0 and column != 7:
                pointer = i - SIDE_LENGTH + 1
                while True:
                    if field[pointer] == 'R' or field[pointer] == 'B':
                        break
                    field[pointer] = 'x'

                    if pointer // SIDE_LENGTH == 0 or pointer % SIDE_LENGTH == 7:
                        break
                    pointer -= SIDE_LENGTH - 1

            if row != 7 and column != 0:
                pointer = i + SIDE_LENGTH - 1
                while pointer < SIDE_LENGTH**2:
                    if field[pointer] == 'R' or field[pointer] == 'B':
                        break
                    field[pointer] = 'x'

                    if pointer % SIDE_LENGTH == 0 or pointer // SIDE_LENGTH == 7:
                        break
                    pointer += SIDE_LENGTH - 1

            if row != 7 and column != 7:
                pointer = i + SIDE_LENGTH + 1
                while pointer < SIDE_LENGTH**2:
                    if field[pointer] == 'R' or field[pointer] == 'B':
                        break
                    field[pointer] = 'x'

                    if pointer // SIDE_LENGTH == 7 or pointer % SIDE_LENGTH == 7:
                        break
                    pointer += SIDE_LENGTH + 1

    res = 0
    for i in field:
        if i == '*':
            res += 1
    print(res)

# d()