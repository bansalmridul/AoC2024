import os
from collections import defaultdict
import numpy as np
import itertools
from pprint import pprint


class Region:
    def __init__(self):
        self.points = set()
        self.area = 0
        self.x_min = 200
        self.x_max = -1
        self.y_min = 200
        self.y_max = -1

    def update(self, row, col):
        self.area += 1
        self.points.add((row, col))
        self.x_min = min(self.x_min, row)
        self.x_max = max(self.x_max, row)
        self.y_min = min(self.y_min, col)
        self.y_max = max(self.y_max, col)

    def __repr__(self):
        # perimeter = 2 * (self.x_max - self.x_min + 1) + 2 * (self.y_max - self.y_min + 1)
        return f"Area: {self.area}, Perimeter: {self.perimeter()}"
        # return (f"Area: {self.area}, {self.x_max} - {self.x_min}, {self.y_max} - {self.y_min}")

    def perimeter(self):
        perimeter = 0
        for point, diff in itertools.product(self.points, [(0, 1), (1, 0), (0, -1), (-1, 0)]):
            n_point = (point[0] + diff[0], point[1] + diff[1])
            if n_point not in self.points:
                perimeter += 1
        return perimeter

    def sides(self):
        sides = 0
        u_sides_visited = set()
        d_sides_visited = set()
        l_sides_visited = set()
        r_sides_visited = set()

        for point in self.points:
            n_point = (point[0] + 1, point[1])
            if n_point not in self.points:  # check if a bottom edge
                left = (point[0], point[1] - 1) not in d_sides_visited
                right = (point[0], point[1] + 1) not in d_sides_visited
                d_sides_visited.add(point)
                if left and right:
                    sides += 1
                elif not left and not right:
                    sides -= 1
            n_point = (point[0] - 1, point[1])
            if n_point not in self.points:  # check if a upper edge
                left = (point[0], point[1] - 1) not in u_sides_visited
                right = (point[0], point[1] + 1) not in u_sides_visited
                u_sides_visited.add(point)
                if left and right:
                    sides += 1
                elif not left and not right:
                    sides -= 1
            n_point = (point[0], point[1] + 1)
            if n_point not in self.points:  # check if a right edge
                upper = (point[0] - 1, point[1]) not in r_sides_visited
                lower = (point[0] + 1, point[1]) not in r_sides_visited
                r_sides_visited.add(point)
                if upper and lower:
                    sides += 1
                elif not upper and not lower:
                    sides -= 1
            n_point = (point[0], point[1] - 1)
            if n_point not in self.points:  # check if a left edge
                upper = (point[0] - 1, point[1]) not in l_sides_visited
                lower = (point[0] + 1, point[1]) not in l_sides_visited
                l_sides_visited.add(point)
                if upper and lower:
                    sides += 1
                elif not upper and not lower:
                    sides -= 1
        return sides


def getRegions(grid):
    rows, cols = len(grid), len(grid[0])
    visited = np.zeros((rows, cols), dtype=bool)
    retDict = defaultdict(Region)
    idx = 1

    def dfs(row, col, char, visited, reg):
        if not visited[row][col] and grid[row][col] == char:
            visited[row][col] = True
            reg.update(row, col)
            for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                nr, nc = row + dr, col + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    dfs(nr, nc, char, visited, reg)

    for row, col in np.ndindex(grid.shape):
        char = grid[row][col]
        if not visited[row][col]:
            idx += 1
            r = Region()
            dfs(row, col, char, visited, r)
            retDict[idx] = r

    return retDict


def part1and2(test=False):
    fn = os.path.basename(__file__)
    if test:
        fn = f"input{fn[:-3]}-t.txt"
    else:
        fn = f"input{fn[:-3]}.txt"
    file1 = open(fn, "r+")
    lines = file1.readlines()
    grid = np.zeros((len(lines), len(lines[0]) - 1), dtype=str)
    for i, line in enumerate(lines):
        grid[i] = np.char.array(list(line.strip()))
    ret1 = 0
    ret2 = 0
    reges = getRegions(grid)
    # pprint(reges)
    for _, region in reges.items():
        ret1 += region.area * region.perimeter()
        ret2 += region.area * region.sides()
    print(ret1)
    print(ret2)


if __name__ == "__main__":
    part1and2()
