import os, time
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


def get_ds_opt(disk_space):
    max_len = len(disk_space) - 1
    min_val = disk_space[-1][0]
    min_val_pos = max_len  # length where earliest position occurs
    disk_space_opt = deque()
    for x in range(max_len, -1, -1):
        if disk_space[x] and disk_space[x][0] < min_val:
            min_val = disk_space[x][0]
            min_val_pos = x
        disk_space_opt.appendleft((min_val, min_val_pos))  # index, length
    return disk_space_opt


def part2(test=False):
    fn = os.path.basename(__file__)
    if test:
        fn = f"input{fn[:-3]}-t.txt"
    else:
        fn = f"input{fn[:-3]}.txt"
    file1 = open(fn, "r+")
    line = file1.readlines()[0].strip()

    disk_file = defaultdict(Triple)  # set of all disks
    v = 0
    ind = 0
    b = True
    disk_space = deque()
    [disk_space.append([]) for _ in range(10)]  # index maps to minHeap of all spaces with length index
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
    disk_space_opt = get_ds_opt(disk_space)

    for v in range(len(disk_file) - 1, -1, -1):
        t = disk_file[v]
        if t.length >= len(disk_space_opt):  # check if any space is long enough to contain file
            continue
        block = disk_space_opt[t.length]  # get index of earliest space that fits file, and the length of that space
        if t.index < block[0]:  # only continue if index of space is before file
            continue
        rem_length = block[1] - t.length  # remaining length after file moves into the space
        t.index = block[0]  # set the index of the file to the index of the space
        heappop(disk_space[block[1]])  # space no longer has the length, as the file has moved in
        heappush(disk_space[rem_length], block[0] + t.length)  # space now has length of rem_length, at index=old_index + length of file

        while not disk_space[-1]:  # if no spaces of given length
            disk_space.pop()  # remove that length from disk space

        max_len = len(disk_space) - 1
        min_val = disk_space[-1][0]
        min_val_pos = max_len  # length where earliest position occurs
        disk_space_opt = deque()
        disk_space_opt = get_ds_opt(disk_space)

    print(checksum2(disk_file))


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
