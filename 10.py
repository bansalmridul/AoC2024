import math
import os
from collections import defaultdict, deque
import itertools
import numpy as np

dir = [[0,1], [1,0], [0,-1], [-1, 0]]

class Position:
    def __init__(self, l, v, c=1):
        self.x = l
        self.y = v
        self.count = 1
    
    def __str__(self) -> str:
        return f"({self.length}, {self.value})"

    def __repr__(self) -> str:
        return f"({self.length}, {self.value})"

    def __hash__(self):
        return hash((self.x, self.y))

    def __eq__(self, obj):
        if not isinstance(other, Position):
            return False
        return obj.x == self.x and obj.y == self.y

def part1(test=False):
    fn = os.path.basename(__file__)
    if test:
        fn = f"input{fn[:-3]}-t.txt"
    else:
        fn = f"input{fn[:-3]}.txt"
    file1 = open(fn, "r+")
    arrt = file1.readlines()
    grid = []
    height_dict = defaultdict(set)
    for i, line in enumerate(arrt):
        row = [int(char) for char in line if char.isdigit()]
        for j, height in enumerate(row):
            height_dict[height].add((i, j))
        grid.append(row)
    trailheads = height_dict[0]
    ret = 0
    for th in trailheads:
        pos = set()
        pos.add(th)
        for i in range(1, 10, 1):
            next_pos = set()
            for c_pos in pos:
                for d in dir:
                    n_pos = (c_pos[0]+ d[0], c_pos[1] + d[1])
                    if n_pos in height_dict[i]:
                        next_pos.add(n_pos)
            pos = next_pos
        ret += len(pos)
    print(ret)

def part2(test=False):
    fn = os.path.basename(__file__)
    if test:
        fn = f"input{fn[:-3]}-t.txt"
    else:
        fn = f"input{fn[:-3]}.txt"
    file1 = open(fn, "r+")
    arrt = file1.readlines()
    grid = []
    height_dict = defaultdict(set)
    for i, line in enumerate(arrt):
        row = [int(char) for char in line if char.isdigit()]
        for j, height in enumerate(row):
            height_dict[height].add((i, j))
        grid.append(row)
    ret = np.zeros((len(grid), len(grid[0])), dtype = int)
    for pos in height_dict[0]:
        ret[pos] += 1
    for i in range(1, 10, 1):
        next_ret = np.zeros((len(grid), len(grid[0])), dtype = int)
        next_set = height_dict[i]
        for pos in height_dict[i-1]:
            for d in dir:
                n_pos = (pos[0]+ d[0], pos[1] + d[1])
                if n_pos in next_set:
                    next_ret[n_pos] += ret[pos]
        ret = next_ret
    print(np.sum(ret))

if __name__ == "__main__":
    part1()
    part2()
