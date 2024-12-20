import os
import numpy as np
import itertools
import time
dir_list = [(0, -1), (0, 1), (-1, 0), (1, 0)]

def dfs(grid, s_val):
    index = np.where(grid == s_val)
    sx, sy = index[0][0], index[1][0]
    index = np.where(grid == 0)
    x, y = index[0][0], index[1][0]
    while not (x == sx and y == sy):
        dist = grid[x][y]
        for dir in dir_list:
            nx, ny = x+dir[0], y+dir[1]
            if grid[nx][ny] > dist:
                grid[nx][ny] = dist + 1
                x, y = nx, ny
                break
    return 1

def saves_threshold(grid, t):
    ret = 0
    for x, y in np.ndindex(grid.shape):
        for dir in dir_list:
            ht = grid[x][y] #honest time
            if ht < t: #not enough time to save
                continue
            p1x, p1y = x + dir[0], y+dir[1]
            if (not (0 < p1x < len(grid) - 1)) or (not (0 < p1y < len(grid[0]) - 1)) or grid[p1x][p1y] >= 0: #border coord or not a barrier
                continue
            p2x, p2y = x + 2*dir[0], y+2*dir[1]
            #t <= ts = ht - grid(p2) - 2
            if (not (0 < p2x < len(grid) - 1)) or (not (0 < p2y < len(grid[0]) - 1)) or -1 == grid[p2x][p2y] or ht - grid[p2x][p2y] - 2 < t: #border coord or barrier or insufficient time save
                continue
            ret += 1
    return ret

#alternative solution is to grid a map of dist to point, and iterate through all of the points that are at least
#threshold away. Then check if in range and if it saves t time
#would implement this, but I'm tired and my solution works quickly enough
def saves_threshold_extra(grid, t):
    ret = 0
    index = np.where(grid == 0)
    ex, ey = index[0][0], index[1][0]
    for x, y in np.ndindex(grid.shape):
        ht = grid[x][y] #honest time
        if ht < t + abs(x - ex) + abs(y - ey): continue #ht must be at least dist more than threshold to save time
        for dx in range(-20, 21, 1):
            for dy in range(-1 * (20 - abs(dx)), (21 - abs(dx)), 1): #iterate through all points up to dist20 away
                cx, cy = x + dx, y + dy #cheat x, y
                if cx < 0 or cx >= len(grid) or cy < 0 or cy >= len(grid[0]) or grid[cx][cy] == -1: continue #not in grid or barrier
                cheat_dist = abs(dx) + abs(dy)
                if ht - grid[cx][cy] - cheat_dist >= t:
                    ret += 1
    return ret
        

def part1and2(test=False):
    fn = os.path.basename(__file__)
    if test:
        fn = f"input{fn[:-3]}-t.txt"
        #s_val and def_val are arbitrarily large, specific value doesn't matter
        t, t2, s_val, def_val = 10, 68, 300, 100
    else:
        fn = f"input{fn[:-3]}.txt"
        t, t2, s_val, def_val = 100, 100, 7_000_000, 5_000_000
    file1 = open(fn, "r+")
    lines = file1.readlines()
    convert = {'#': -1, 'E': 0, 'S': s_val}
    grid = np.array([convert.get(c, def_val) for c in lines[0].strip()]).reshape(1, -1)
    ret = 0
    for line in lines[1:]:
        row = np.array([convert.get(c, def_val) for c in line.strip()]).reshape(1, -1)
        grid = np.vstack((grid, row))
    dfs(grid, s_val)
    print(saves_threshold(grid, t))
    print(saves_threshold_extra(grid, t2))

    
     
if __name__ == "__main__":
    t = time.perf_counter()
    part1and2()
    print(f"Time: {time.perf_counter() - t}")