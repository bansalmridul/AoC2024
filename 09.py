import math
import os
from collections import defaultdict, deque
import itertools


class Pair:
    def __init__(self, l, v):
        self.length = l
        self.value = v

    def __str__(self) -> str:
        return f"({self.length}, {self.value})"

    def __repr__(self) -> str:
        return f"({self.length}, {self.value})"


def checksum(disk_final):
    ind = 0
    ret = 0
    while disk_final:
        p = disk_final.popleft()
        if p.value == -1:
            ind += p.length
            continue
        ret += (ind + (ind + p.length - 1)) * p.length * p.value // 2
        ind += p.length
    return ret


def part1(test=False):
    fn = os.path.basename(__file__)
    if test:
        fn = f"input{fn[:-3]}-t.txt"
    else:
        fn = f"input{fn[:-3]}.txt"
    file1 = open(fn, "r+")
    line = file1.readlines()[0].strip()

    disk = deque()
    disk_final = deque()
    ind = 0
    b = True
    for c in line:
        if b:
            disk.append(Pair(int(c), ind))
            ind += 1
        else:
            disk.append(Pair(int(c), -1))
        b = not b
    while disk:
        while disk and disk[0].value != -1:
            disk_final.append(disk.popleft())
        while disk and disk[-1].value == -1:
            disk.pop()
        if not disk:
            break
        space = disk[0]
        file = disk[-1]
        if space.length > file.length:
            disk_final.append(disk.pop())
            space.length = space.length - file.length
        elif space.length < file.length:
            disk_final.append(Pair(space.length, file.value))
            disk.popleft()
            file.length = file.length - space.length
        else:
            disk_final.append(disk.pop())
            space.length = space.length - file.length
            disk.popleft()

    print(checksum(disk_final))


def part2(test=False):
    fn = os.path.basename(__file__)
    if test:
        fn = f"input{fn[:-3]}-t.txt"
    else:
        fn = f"input{fn[:-3]}.txt"
    file1 = open(fn, "r+")
    line = file1.readlines()[0].strip()

    disk = deque()
    disk_final = deque()
    ind = 0
    b = True
    for c in line:
        if b:
            disk.append(Pair(int(c), ind))
            ind += 1
        else:
            disk.append(Pair(int(c), -1))
        b = not b
    ind = len(disk) - 1
    while True:
        while ind >= 0 and disk[ind].value == -1:
            ind -= 1
        if ind < 0:
            break
        p = disk[ind]
        j = 0
        pc = disk[j]
        print(ind, p)
        while j < ind and not (pc.value == -1 and pc.length >= p.length):
            j += 1
            pc = disk[j]
        if j == ind:
            ind -= 1
            continue
        if pc.length == p.length:
            pc.value = p.value
        else:
            np = Pair(pc.length - p.length, -1)
            pc.length, pc.value = p.length, p.value
            disk.insert(j + 1, np)
        p.value = -1
        # print(disk)

    print(checksum(disk))


if __name__ == "__main__":
    # part1()
    part2()
