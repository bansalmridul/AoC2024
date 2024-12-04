import bisect
import re

def part1(test=False):
    if test:
        fn = f'input{__file__[:-3]}-t.txt'
    else:
        fn = f'input{__file__[:-3]}.txt'
    file1 = open(fn, 'r+')
    arrt = file1.readlines()
    ret = 0
    pattern = r"mul\(\d+,\d+\)"
    for line in arrt:
        matches = re.findall(pattern, line)
        for match in matches:
            num1, num2 = map(int, re.search(r"mul\((\d+),(\d+)\)", match).groups())
            ret += num1*num2
    print(ret)

def part2(test=False):
    if test:
        fn = f'input{__file__[:-3]}-t2.txt'
    else:
        fn = f'input{__file__[:-3]}.txt'
    file1 = open(fn, 'r+')
    arrt = file1.readlines()
    ret = 0
    pat_mul = r"mul\(\d+,\d+\)"
    pat_do = r"do\(\)"
    pat_dont = r"don't\(\)"
    do_inds = [-1]
    dont_inds = []
    for line in arrt:
        mul_matches = re.finditer(pat_mul, line)
        do_matches = re.finditer(pat_do, line)
        dont_matches = re.finditer(pat_dont, line)
        for match in do_matches:
            start, end = match.span()
            do_inds.append(start)
        for match in dont_matches:
            start, end = match.span()
            dont_inds.append(start)
        for match in mul_matches:
            start, end = match.span()
            do_val = bisect.bisect(do_inds, start)
            dont_val = bisect.bisect(dont_inds, start)
            print(start, do_val, dont_val)
            if dont_val == 0 or do_inds[do_val - 1] > dont_inds[dont_val - 1]:
                num1, num2 = map(int, re.search(r"mul\((\d+),(\d+)\)", line[start:end]).groups())
                ret += num1*num2            
    print(ret)

if __name__ == '__main__':
    part1()
    part2()

