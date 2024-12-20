import os, time
import math
from collections import defaultdict
import itertools


def part1(test=False):
    fn = os.path.basename(__file__)
    if test:
        fn = f"input{fn[:-3]}-t.txt"
    else:
        fn = f"input{fn[:-3]}.txt"
    file1 = open(fn, "r+")
    arrt = file1.readlines()
    ret = set()
    antennas = defaultdict(list)
    height = len(arrt)
    width = len(arrt[0].strip())
    for i, line in enumerate(arrt):
        line = line.strip()
        for j, c in enumerate(line):
            if c != ".":
                antennas[c].append((i, j))
    for ant, poses in antennas.items():
        for x, y in itertools.combinations(poses, 2):
            diff = (x[0] - y[0], x[1] - y[1])
            p1 = (x[0] + diff[0], x[1] + diff[1])
            p2 = (y[0] - diff[0], y[1] - diff[1])
            if 0 <= p1[0] < height and 0 <= p1[1] < width:
                ret.add(p1)
            if 0 <= p2[0] < height and 0 <= p2[1] < width:
                ret.add(p2)
    print(len(ret))


def part2(test=False):
    fn = os.path.basename(__file__)
    if test:
        fn = f"input{fn[:-3]}-t.txt"
    else:
        fn = f"input{fn[:-3]}.txt"
    file1 = open(fn, "r+")
    arrt = file1.readlines()
    ret = set()
    antennas = defaultdict(list)
    height = len(arrt)
    width = len(arrt[0].strip())
    for i, line in enumerate(arrt):
        line = line.strip()
        for j, c in enumerate(line):
            if c != ".":
                antennas[c].append((i, j))
    for ant, poses in antennas.items():
        for x, y in itertools.combinations(poses, 2):
            diff = (x[0] - y[0], x[1] - y[1])
            d = math.gcd(diff[0], diff[1])
            diff = (diff[0] // d, diff[1] // d)
            curr = x
            while 0 <= curr[0] < height and 0 <= curr[1] < width:
                ret.add(curr)
                curr = (curr[0] + diff[0], curr[1] + diff[1])
            curr = (x[0] - diff[0], x[1] - diff[1])
            while 0 <= curr[0] < height and 0 <= curr[1] < width:
                ret.add(curr)
                curr = (curr[0] - diff[0], curr[1] - diff[1])
    print(len(ret))


def main():
    t = time.perf_counter()
    part1()
    t1 = time.perf_counter()
    print(f"Time 1: {t1 - t}")
    part2()
    t2 = time.perf_counter()
    print(f"Time 2: {t2 - t1}")


if __name__ == "__main__":
    main()
