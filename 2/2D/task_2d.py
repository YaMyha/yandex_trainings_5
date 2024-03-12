def d():
    n = int(input())
    square_sides_num = 4
    side_size = 8

    cells = [[-1 for i in range(side_size+2)] for j in range(side_size+2)]
    figure_cells = [list(map(lambda x: int(x), input().split())) for _ in range(n)]
    for item in figure_cells:
        cells[item[0]][item[1]] = 1
    dx_list = [-1, 0, 1, 0]
    dy_list = [0, 1, 0, -1]

    perimeter = square_sides_num * len(figure_cells)
    for x, y in figure_cells:
        for i in range(4):
            curr_cell = cells[x+dx_list[i]][y+dy_list[i]]
            if curr_cell == 1:
                perimeter -= 1
    print(perimeter)

d()
if __name__ == "__main__":
    d()