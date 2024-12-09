import math
import os
from collections import defaultdict, deque
from heapq import heapify, heappush, heappop


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

class Triple:
    def __init__(self, l, i):
        self.length = l
        self.index = i

    def __str__(self) -> str:
        return f"({self.length},{self.index})"

    def __repr__(self) -> str:
        return f"({self.length}, {self.index})"

def checksum2(disk_file):
    ret = 0
    for key, value in disk_file.items():
        ret += key * value.length * (value.index + (value.index + value.length - 1)) // 2
    return ret


def part2(test=False):
    fn = os.path.basename(__file__)
    if test:
        fn = f"input{fn[:-3]}-t.txt"
    else:
        fn = f"input{fn[:-3]}.txt"
    file1 = open(fn, "r+")
    line = file1.readlines()[0].strip()

    disk_file = defaultdict(Triple) #set of all disks
    disk_space = [] #index maps to minHeap of all spaces with length index
    v = 0
    ind = 0
    b = True
    disk_space = deque()
    [disk_space.append([]) for _ in range(10)]
    for c in line:
        if b:
            disk_file[v] = Triple(int(c), ind)
            v += 1
        else:
            heappush(disk_space[int(c)], ind)
        ind += int(c)
        b = not b
    
    while not disk_space[-1]:
        disk_space.pop()
    max_len = len(disk_space) - 1
    min_val = disk_space[-1][0]
    min_val_pos = max_len #length where earliest position occurs
    disk_space_opt = deque()
    for x in range(max_len + 1):
        if disk_space[max_len - x] and min_val > disk_space[max_len - x][0]:
                min_val = disk_space[max_len - x][0]
                min_val_pos = max_len - x
        disk_space_opt.appendleft((min_val, min_val_pos)) #index, length
    #print(disk_space)
    #print(disk_file)
    #print(disk_space_opt)
    for v in range(len(disk_file) - 1, -1 , -1):
        t = disk_file[v]
        if t.length >= len(disk_space_opt):
            continue
        block = disk_space_opt[t.length]
        rem_length = block[1] - t.length
        t.index = block[0]
        heappop(disk_space[block[1]]) 
        heappush(disk_space[rem_length], block[0] + t.length)
        
        while not disk_space[-1]:
            disk_space.pop()
            disk_space_opt.pop()
        max_len = len(disk_space) - 1
        min_val = disk_space[-1][0]
        min_val_pos = max_len
        for x in range(max_len, -1, -1):
            if disk_space[x] and disk_space[x][0] < min_val:
                min_val = disk_space[x][0]
                min_val_pos = x
            disk_space_opt[x] = (min_val, min_val_pos) #index, length
        #print(v)
        #print(disk_file)
        #print(disk_space)
        #print(disk_space_opt)
    print(checksum2(disk_file))

if __name__ == "__main__":
    # part1()
    part2(True)
