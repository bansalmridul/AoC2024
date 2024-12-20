import os, time
import numpy as np

dir_map = [(0, 1), (-1, 0), (0, -1), (1, 0)]
turn = 1000
max_int64 = np.iinfo(np.int64).max


def printGrid(grid):
    for line in grid:
        print("".join(line))


def bfs(grid, score, x, y, d):
    next_set = set()  # set of all points to be visited
    next_set.add((x, y, d))
    score[x][y][d] = 0
    while next_set:
        x, y, d = next_set.pop()
        for i in range(4):  # could just unroll this tbh
            dir = dir_map[d]
            if i == d and grid[x + dir[0]][y + dir[1]] != "#":  # available to move
                if score[x + dir[0]][y + dir[1]][d] > score[x][y][d] + 1:  # decreases score
                    score[x + dir[0]][y + dir[1]][d] = score[x][y][d] + 1
                    next_set.add((x + dir[0], y + dir[1], i))
            if (d - i) % 2 == 1:  # 90 degree turn
                if score[x][y][i] > score[x][y][d] + turn:  # decreases score
                    score[x][y][i] = score[x][y][d] + turn
                    next_set.add((x, y, i))


def dfs(score, ex, ey, d):
    optimal_points = set()
    queue = {(ex, ey, d)}
    while queue:
        row, col, dir = queue.pop()
        if (row, col, dir) in optimal_points:
            print("shouldn't be here")
            continue
        optimal_points.add((row, col))
        c_score = score[row][col][dir]
        if score[row - dir_map[dir][0]][col - dir_map[dir][1]][dir] == c_score - 1:
            queue.add((row - dir_map[dir][0], col - dir_map[dir][1], dir))
        if score[row][col][(dir - 1) % 4] == c_score - turn:
            queue.add((row, col, (dir - 1) % 4))
        if score[row][col][(dir + 1) % 4] == c_score - turn:
            queue.add((row, col, (dir + 1) % 4))

    return optimal_points


def part1and2(test=False):
    fn = os.path.basename(__file__)
    if test:
        fn = f"input{fn[:-3]}-t.txt"
    else:
        fn = f"input{fn[:-3]}.txt"
    file1 = open(fn, "r+")
    lines = file1.readlines()
    grid = np.char.array(list(lines[0].strip())).reshape(1, -1)
    ret = 0
    for line in lines[1:]:
        row = np.char.array(list(line.strip())).reshape(1, -1)
        grid = np.vstack((grid, row))
    index = np.where(grid == "S")
    x, y, d = index[0][0], index[1][0], 0
    index = np.where(grid == "E")
    ex, ey = index[0][0], index[1][0]
    score = np.full((len(grid), len(grid[0]), 4), max_int64 - 1, dtype=np.int64)
    bfs(grid, score, x, y, d)
    arg_min = np.argmin(score[ex][ey])
    print(score[ex][ey][arg_min])
    opt_points = dfs(score, ex, ey, arg_min)  # assumes only one min, but valid for this problem
    print(len(opt_points))


def main():
    t = time.perf_counter()
    part1and2()
    print(f"Time: {time.perf_counter() - t}")


if __name__ == "__main__":
    main()
