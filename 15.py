import math
import os
import numpy as np

dir_map = {
    "<": (0, -1),
    ">": (0, 1),
    "^": (-1, 0),
    "v": (1, 0),
}
np.set_printoptions(linewidth=np.inf)


def printGrid(grid):
    for line in grid:
        print("".join(line))


def move(grid, dir, x, y):
    d = dir_map[dir]
    nx, ny = x + d[0], y + d[1]
    while grid[nx][ny] in "O[]":
        nx, ny = nx + d[0], ny + d[1]
    if grid[nx][ny] == "#":
        return x, y
    while not (nx == x and ny == y):
        px, py = nx - d[0], ny - d[1]
        grid[nx][ny] = grid[px][py]
        nx, ny = px, py
    grid[x][y] = "."
    x, y = x + d[0], y + d[1]
    return x, y


def calculate(grid):
    ret = 0
    indices = np.where(grid == "O")
    for x, y in zip(indices[0], indices[1]):
        ret += 100 * x + y
    return ret


def calculate2(grid):
    ret = 0
    indices = np.where(grid == "[")
    for x, y in zip(indices[0], indices[1]):
        ret += 100 * x + y
    return ret


def part1(test=False):
    fn = os.path.basename(__file__)
    if test:
        fn = f"input{fn[:-3]}-t.txt"
    else:
        fn = f"input{fn[:-3]}.txt"
    file1 = open(fn, "r+")
    lines = file1.readlines()
    grid = np.char.array(list(lines[0].strip())).reshape(1, -1)
    b = True
    x, y = -1, -1
    for line in lines[1:]:
        if line == "\n":
            b = False
            index = np.where(grid == "@")
            x, y = index[0][0], index[1][0]
            continue
        if b:
            row = np.char.array(list(line.strip())).reshape(1, -1)
            grid = np.vstack((grid, row))
        else:
            for c in line.strip():
                x, y = move(grid, c, x, y)
    print(calculate(grid))


def createDoubleLine(line):
    ret = np.zeros(len(line) * 2, dtype=str)
    for i, c in enumerate(line):
        if c == "#":
            ret[2 * i] = "#"
            ret[2 * i + 1] = "#"
        elif c == "O":
            ret[2 * i] = "["
            ret[2 * i + 1] = "]"
        elif c == "@":
            ret[2 * i] = "@"
            ret[2 * i + 1] = "."
        elif c == ".":
            ret[2 * i] = "."
            ret[2 * i + 1] = "."
    return ret


def move2(grid, dir, x, y):
    d = dir_map[dir]
    x_dict = dict()  # maps each row to list of affected cols
    x_dict[x] = {y}
    c_row = x

    while True:
        n_row = c_row + d[0]
        n_set = set()
        for ty in x_dict[c_row]:  # iterate through all affected cols in curr row, but on next row
            if grid[n_row][ty] == "#":  # cannot move
                return x, y
            if grid[n_row][ty] == "[":
                n_set.add(ty)
                n_set.add(ty + 1)
            if grid[n_row][ty] == "]":
                n_set.add(ty)
                n_set.add(ty - 1)
        c_row = n_row  # set curr as next
        if len(n_set) == 0:
            break
        x_dict[c_row] = n_set  # update dict

    while not c_row == x:
        p_row = c_row - d[0]
        for ty in x_dict[p_row]:
            grid[c_row][ty] = grid[p_row][ty]
            grid[p_row][ty] = "."
        c_row = p_row
    return x + d[0], y


def part2(test=False):
    fn = os.path.basename(__file__)
    if test:
        fn = f"input{fn[:-3]}-t.txt"
    else:
        fn = f"input{fn[:-3]}.txt"
    file1 = open(fn, "r+")
    lines = file1.readlines()
    grid = createDoubleLine(lines[0].strip()).reshape(1, -1)
    b = True
    x, y = -1, -1
    for line in lines[1:]:
        if line == "\n":
            b = False
            index = np.where(grid == "@")
            x, y = index[0][0], index[1][0]
            continue
        if b:
            row = createDoubleLine(line.strip()).reshape(1, -1)
            grid = np.vstack((grid, row))
        else:
            for c in line.strip():
                if c == "<" or c == ">":
                    x, y = move(grid, c, x, y)
                else:
                    x, y = move2(grid, c, x, y)
    print(calculate2(grid))


if __name__ == "__main__":
    part1()
    part2()
