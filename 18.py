import os
import numpy as np
from heapq import heapify, heappush, heappop

dir_list = [(0, -1), (0, 1), (-1, 0), (1, 0)]

def dijkstra(grid):
    minScores = len(grid) ** 2 * np.ones((len(grid), len(grid)), dtype=int)
    x, y = 0, 0
    up_next = [(0, x, y)]
    minScores[x][y] = 0
    heapify(up_next)
    while up_next:
        s, x, y = heappop(up_next)
        for dx, dy in dir_list:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == 0 and minScores[nx][ny] > s + 1:
                minScores[nx][ny] = s + 1
                heappush(up_next, (s + 1, nx, ny))
    return minScores[-1][-1]

def bfs(grid): #i don't know what is faster, this or keeping track of all valid paths and removing valid paths until none remain
    x, y = 0, 0
    visited = set()
    up_next = {(x, y)}
    while up_next:
        #print(up_next)
        x, y = up_next.pop()
        visited.add((x, y))
        for dx, dy in dir_list:
            nx, ny = x + dx, y + dy
            if nx == len(grid) - 1 and ny == len(grid) - 1:
                return True
            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == 0 and (nx,ny) not in visited:
                up_next.add((nx, ny))
    return False

def part1and2(test=False):
    fn = os.path.basename(__file__)
    if test:
        fn = f"input{fn[:-3]}-t.txt"
        width = 7
        count = 12
    else:
        fn = f"input{fn[:-3]}.txt"
        width = 71
        count = 1024
    file1 = open(fn, "r+")
    lines = file1.readlines()
    points = []
    for line in lines:
        points.append([int(x) for x in line.split(',')])
    grid = np.zeros((width, width), dtype = int)
    for point in points[:count]:
        grid[point[0]][point[1]] = 1
    print(dijkstra(grid))
    left = count
    right = len(lines)
    prev = left
    while right - left > 1:
        mid = (left + right) // 2
        if mid > prev: #need to add points
            for point in points[prev:mid]:
                grid[point[0]][point[1]] = 1
        else:
            for point in points[mid:prev+1]: #remove points
                grid[point[0]][point[1]] = 0
        #print(grid)
        b = bfs(grid)
        #print(b, left, right)
        if b:
            left = mid
        else:
            right = mid
        prev = mid
    print(lines[left][:-1])


if __name__ == "__main__":
    part1and2()
