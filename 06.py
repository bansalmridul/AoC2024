import os
import math
from collections import defaultdict
import numpy as np
from pprint import pprint
import itertools

dir_map = {"U": (-1, 0), "D": (1, 0), "R": (0, 1), "L": (0, -1)}
dir_arr = ["U", "R", "D", "L"]


def part1(test=False):
    fn = os.path.basename(__file__)
    if test:
        fn = f"input{fn[:-3]}-t.txt"
    else:
        fn = f"input{fn[:-3]}.txt"
    file1 = open(fn, "r+")
    arrt = file1.readlines()

    map = []
    x = -1
    y = -1
    dir = 0
    for i, line in enumerate(arrt):
        line = line.strip()
        if "^" in line:
            x = i
            y = line.index("^")
        map.append(list(line))
    map[x][y] = "."

    ret = 0
    while True:
        xn = x + dir_map[dir_arr[dir]][0]
        yn = y + dir_map[dir_arr[dir]][1]
        if map[x][y] == ".":
            map[x][y] = "X"
            ret += 1
        if xn < 0 or xn >= len(map):
            break
        if yn < 0 or yn >= len(map[0]):
            break
        if map[xn][yn] == "#":
            map[x][y] = "+"
            dir = (dir + 1) % 4
        else:
            x = xn
            y = yn
    print(ret)


def traverse(map, x, y):
    dir = 0
    visited = defaultdict(list)
    while True:
        xn = x + dir_map[dir_arr[dir]][0]
        yn = y + dir_map[dir_arr[dir]][1]
        if (x, y) in visited[dir]:
            return 1
        visited[dir].append((x, y))
        if xn < 0 or xn >= len(map):
            break
        if yn < 0 or yn >= len(map[0]):
            break
        if map[xn][yn] == "#":
            dir = (dir + 1) % 4
        else:
            x = xn
            y = yn
    return 0


def part2(test=False):
    fn = os.path.basename(__file__)
    if test:
        fn = f"input{fn[:-3]}-t.txt"
    else:
        fn = f"input{fn[:-3]}.txt"
    file1 = open(fn, "r+")
    arrt = file1.readlines()

    map = []
    x = -1
    y = -1
    dir = 0
    for i, line in enumerate(arrt):
        line = line.strip()
        if "^" in line:
            sx = i
            sy = line.index("^")
        map.append(list(line))
    map[sx][sy] = "."

    ret = 0
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == "#" or (i == sx and j == sy):
                continue
            print(i, j)
            map[i][j] = "#"
            ret += traverse(map, sx, sy)
            map[i][j] = "."

    print(ret)


if __name__ == "__main__":
    part1()
    part2()
