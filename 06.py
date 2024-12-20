import os, time

dir_map = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def part1(test=False):
    fn = os.path.basename(__file__)
    if test:
        fn = f"input{fn[:-3]}-t.txt"
    else:
        fn = f"input{fn[:-3]}.txt"
    file1 = open(fn, "r+")
    arrt = file1.readlines()

    map = []
    for i, line in enumerate(arrt):
        line = line.strip()
        if "^" in line:
            x, y = i, line.index("^")
        map.append(list(line))
    print(len(get_spots(map, x, y)) + 1)


def traverse(map, x, y):
    dir = 0
    visited = [set() for _ in range(4)]
    while True:
        xn = x + dir_map[dir][0]
        yn = y + dir_map[dir][1]
        if (x, y) in visited[dir]:
            return 1
        visited[dir].add((x, y))
        if xn < 0 or xn >= len(map):
            break
        if yn < 0 or yn >= len(map[0]):
            break
        if map[xn][yn] == "#":
            dir = (dir + 1) % 4
        else:
            x, y = xn, yn
    return 0


def get_spots(map, x, y):
    dir = 0
    visited = set()
    while True:
        xn = x + dir_map[dir][0]
        yn = y + dir_map[dir][1]
        if xn < 0 or xn >= len(map):
            break
        if yn < 0 or yn >= len(map[0]):
            break
        if map[xn][yn] == "#":
            dir = (dir + 1) % 4
        else:
            x, y = xn, yn
            visited.add((x, y))
    return visited


def part1and2(test=False):
    fn = os.path.basename(__file__)
    if test:
        fn = f"input{fn[:-3]}-t.txt"
    else:
        fn = f"input{fn[:-3]}.txt"
    file1 = open(fn, "r+")
    arrt = file1.readlines()

    map = []
    for i, line in enumerate(arrt):
        line = line.strip()
        if "^" in line:
            sx = i
            sy = line.index("^")
        map.append(list(line))
    map[sx][sy] = "."
    set_pos = get_spots(map, sx, sy)
    print(len(set_pos) + 1)
    ret = 0
    for i, j in set_pos:
        map[i][j] = "#"
        ret += traverse(map, sx, sy)
        map[i][j] = "."
    print(ret)


def main():
    t = time.perf_counter()
    part1and2()
    print(f"Time: {time.perf_counter() - t}")


if __name__ == "__main__":
    main()
