import math
import os


def compare(target, vals=[]):
    if len(vals) == 1:
        return target == vals[0]
    b = False
    if target % vals[-1] == 0:
        b = compare(target // vals[-1], vals[:-1])
    return b or compare(target - vals[-1], vals[:-1])


def backmatch(target, val):
    while val > 0:
        # print(target, val)
        if target % 10 == val % 10:
            target = target // 10
            val = val // 10
        else:
            return -1
    return target


def compare2(target, vals=[]):
    if len(vals) == 1:
        return target == vals[0]
    b = False
    if target % vals[-1] == 0:
        b |= compare2(target // vals[-1], vals[:-1])
    if not b and target > vals[-1]:
        b |= compare2(target - vals[-1], vals[:-1])
        b |= compare2(backmatch(target, vals[-1]), vals[:-1])
    return b


def part1(test=False):
    fn = os.path.basename(__file__)
    if test:
        fn = f"input{fn[:-3]}-t.txt"
    else:
        fn = f"input{fn[:-3]}.txt"
    file1 = open(fn, "r+")
    arrt = file1.readlines()
    ret = 0
    for line in arrt:
        line = line.strip()
        line = line.split(":")
        target = int(line[0])
        vals = [int(x) for x in list(filter(bool, line[1].split(" ")))]
        if compare(target, vals):
            ret += target
    print(ret)


def part2(test=False):
    fn = os.path.basename(__file__)
    if test:
        fn = f"input{fn[:-3]}-t.txt"
    else:
        fn = f"input{fn[:-3]}.txt"
    file1 = open(fn, "r+")
    arrt = file1.readlines()
    ret = 0
    for line in arrt:
        line = line.strip()
        line = line.split(":")
        target = int(line[0])
        vals = [int(x) for x in list(filter(bool, line[1].split(" ")))]
        if compare2(target, vals):
            ret += target
    print(ret)


if __name__ == "__main__":
    part1()
    part2()
