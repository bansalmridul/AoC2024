import os, time
from collections import defaultdict


def part1(test=False):
    fn = os.path.basename(__file__)
    if test:
        fn = f"input{fn[:-3]}-t.txt"
    else:
        fn = f"input{fn[:-3]}.txt"
    file1 = open(fn, "r+")
    arrt = file1.readlines()
    arr1 = []
    arr2 = []
    for line in arrt:
        line = line.strip()
        vals = list(filter(bool, line.split(" ")))
        arr1.append(int(vals[0]))
        arr2.append(int(vals[1]))
    arr1 = sorted(arr1)
    arr2 = sorted(arr2)
    ret = 0
    for e1, e2 in zip(arr1, arr2):
        ret += abs(e1 - e2)
    print(ret)


def part2(test=False):
    fn = os.path.basename(__file__)
    if test:
        fn = f"input{fn[:-3]}-t.txt"
    else:
        fn = f"input{fn[:-3]}.txt"
    file1 = open(fn, "r+")
    arrt = file1.readlines()
    arr1 = []
    arr2 = defaultdict(int)
    for line in arrt:
        line = line.strip()
        vals = list(filter(bool, line.split(" ")))
        arr1.append(int(vals[0]))
        arr2[int(vals[1])] += 1
    ret = 0
    for e1 in arr1:
        ret += e1 * arr2[e1]

    print(ret)


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
