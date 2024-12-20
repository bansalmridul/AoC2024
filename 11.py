import os, time
from collections import defaultdict


def part1and2(test=False):
    fn = os.path.basename(__file__)
    if test:
        fn = f"input{fn[:-3]}-t.txt"
    else:
        fn = f"input{fn[:-3]}.txt"
    file1 = open(fn, "r+")
    line = file1.readlines()[0].strip().split(" ")

    stone_line = defaultdict(int)
    for stone in line:
        stone_line[int(stone)] += 1

    for _ in range(25):
        stone_line_next = defaultdict(int)
        for st, count in stone_line.items():
            if st == 0:
                stone_line_next[1] += count
            elif len(str(st)) % 2 == 0:
                l = len(str(st)) // 2
                stone_line_next[int(str(st)[:l])] += count
                stone_line_next[int(str(st)[l:])] += count
            else:
                stone_line_next[2024 * st] += count
        stone_line = stone_line_next
    ret = 0
    for _, count in stone_line.items():
        ret += count
    print(ret)

    for _ in range(50):
        stone_line_next = defaultdict(int)
        for st, count in stone_line.items():
            if st == 0:
                stone_line_next[1] += count
            elif len(str(st)) % 2 == 0:
                l = len(str(st)) // 2
                stone_line_next[int(str(st)[:l])] += count
                stone_line_next[int(str(st)[l:])] += count
            else:
                stone_line_next[2024 * st] += count
        stone_line = stone_line_next
    ret = 0
    for _, count in stone_line.items():
        ret += count
    print(ret)


def main():
    t = time.perf_counter()
    part1and2()
    print(f"Time: {time.perf_counter() - t}")


if __name__ == "__main__":
    main()
