import os, time


def isValid(vals=[]):
    curr = vals[0]
    valid = True
    dec = curr - vals[1] > 0
    for next in vals[1:]:
        diff = curr - next
        valid = 1 <= abs(diff) <= 3 and (diff > 0) is dec
        if not valid:
            return False
        curr = next
    return True


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
        vals = [int(x) for x in list(filter(bool, line.split(" ")))]
        if isValid(vals):
            ret += 1

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
        vals = [int(x) for x in list(filter(bool, line.split(" ")))]
        if isValid(vals):
            ret += 1
            continue
        for i, val in enumerate(vals):
            del vals[i]
            if isValid(vals):
                ret += 1
                break
            vals.insert(i, val)
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
