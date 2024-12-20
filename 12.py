import os, time
import numpy as np
import itertools


def perimeter(points):
    perimeter = 0
    for point, diff in itertools.product(points, [(0, 1), (1, 0), (0, -1), (-1, 0)]):
        n_point = (point[0] + diff[0], point[1] + diff[1])
        if n_point not in points:
            perimeter += 1
    return perimeter


def sides(points):
    sides = 0
    visited = [set() for _ in range(4)]
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    for point, i in itertools.product(points, range(4)):
        n_point = (point[0] + dirs[i][0], point[1] + dirs[i][1])  # move one in a cardinal direction
        side_visited = visited[i]
        if n_point not in points:  # check if adjacent point is in
            # check if opposing vertices have been added to corresponding "side"
            opp1 = (point[0] - ((i + 1) % 2), point[1] - (i % 2)) not in side_visited
            opp2 = (point[0] + ((i + 1) % 2), point[1] + (i % 2)) not in side_visited
            side_visited.add(point)
            sides += -1 + (opp1 + opp2)
    return sides


def getRegions(grid):
    rows, cols = len(grid), len(grid[0])
    visited = np.zeros((rows, cols), dtype=bool)
    retDict = dict()
    idx = 1

    def dfs(row, col, char, visited, points):
        if not visited[row][col] and grid[row][col] == char:
            visited[row][col] = True
            points.add((row, col))
            for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                nr, nc = row + dr, col + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    dfs(nr, nc, char, visited, points)

    for row, col in np.ndindex(grid.shape):
        char = grid[row][col]
        if not visited[row][col]:
            idx += 1
            points = set()
            dfs(row, col, char, visited, points)
            retDict[idx] = points

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
    for _, region in reges.items():
        ret1 += len(region) * perimeter(region)
        ret2 += len(region) * sides(region)
    print(ret1)
    print(ret2)


def main():
    t = time.perf_counter()
    part1and2()
    print(f"Time: {time.perf_counter() - t}")


if __name__ == "__main__":
    main()
