import os, time


def knapsack(pattern, towels):
    count = [0] * (len(pattern) + 1)
    count[0] = 1  # 1 way to have a pattern of length 0
    for i in range(len(count)):
        for towel in towels:
            start_index = i - len(towel)
            if start_index < 0:
                continue
            # print(pattern[start_index:i])
            if pattern[start_index:i] == towel:
                count[i] += count[start_index]
            # print(i, towel, count)
    # print(pattern, count)
    return count[-1]


def part1and2(test=False):
    fn = os.path.basename(__file__)
    if test:
        fn = f"input{fn[:-3]}-t.txt"
    else:
        fn = f"input{fn[:-3]}.txt"
    file1 = open(fn, "r+")
    lines = file1.readlines()
    towels = [x.strip() for x in lines[0].split(",")]
    ret1, ret2 = 0, 0
    for line in lines[2:]:
        c = knapsack(line.strip(), towels)
        ret1 += c > 0
        ret2 += c
    print(ret1)
    print(ret2)


def main():
    t = time.perf_counter()
    part1and2()
    print(f"Time: {time.perf_counter() - t}")


if __name__ == "__main__":
    main()
