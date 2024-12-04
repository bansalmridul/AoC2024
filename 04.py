import numpy as np
import math
import re
from collections import defaultdict

def check_horizontal1(arr):
    ret = 0
    pattern = r"XMAS"
    pattern2 = r"SAMX"
    for line in arr:
        ret += len(re.findall(pattern, line))
        ret += len(re.findall(pattern2, line))
    return ret

XMAS = np.array(['X','M','A','S'])
SAMX = np.array(['S','A','M','X'])

def check_horizontal(arr, i, j):
    ret = 0
    if j > 2:
        t = arr[i][j-3:j+1]
        ret += int(np.array_equal(t, SAMX))
        ret += int(np.array_equal(t, XMAS))
    return ret

def check_vertical(arr, i, j):
    ret = 0
    if i > 2:
        t = arr[i-3:i+1,j]
        ret += int(np.array_equal(t, SAMX))
        ret += int(np.array_equal(t, XMAS))
    return ret

def check_diagonal_f(arr, i, j):
    ret = 0
    if i < 3 or j < 3:
        return 0
    points = [(i-k,j-k) for k in range(4)]
    t = np.array([arr[e] for e in points])
    ret += int(np.array_equal(t, SAMX))
    ret += int(np.array_equal(t, XMAS))
    return ret

def check_diagonal_b(arr, i, j):
    ret = 0
    if i < 3 or j + 3 >= len(arr[i]):
        return 0
    points = [(i-k,j+k) for k in range(4)]
    t = np.array([arr[e] for e in points])
    ret += int(np.array_equal(t, SAMX))
    ret += int(np.array_equal(t, XMAS))
    return ret

def check_all(arr):
    ret = 0
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] == 'X' or arr[i][j] == 'S':
                ret += check_horizontal(arr, i, j)
                ret += check_vertical(arr, i, j)
                ret += check_diagonal_f(arr, i, j)
                ret += check_diagonal_b(arr, i, j)
    return ret

def part1(test=False):
    if test:
        fn = f'input{__file__[:-3]}-t.txt'
        d = 10
    else:
        fn = f'input{__file__[:-3]}.txt'
        d = 140
    file1 = open(fn, 'r+')
    arrt = file1.readlines()
    ret = 0
    arr = np.chararray((1, d))
    arr[:] = 'a'
    for line in arrt:
        line = line.strip()
        arr = np.vstack((arr, list(line)))
    ret += check_all(arr)
    print(ret)

MAS = np.array(['M','A','S'])
SAM = np.array(['S','A','M'])

def check_diagonal(arr, i, j):
    if arr[i][j] != 'A':
        return 0
    if i < 1 or i + 1 >= len(arr) or j < 1 or j + 1 >= len(arr[i]):
        return 0
    points = [(i-k,j+k) for k in range(-1,2)]
    points2 = [(i+k,j+k) for k in range(-1,2)]
    t = np.array([arr[e] for e in points])
    t2 = np.array([arr[e] for e in points2])
    b = np.array_equal(t, SAM) or np.array_equal(t, MAS)
    b = b and (np.array_equal(t2, SAM) or np.array_equal(t2, MAS))
    return int(b)

def part2(test=False):
    if test:
        fn = f'input{__file__[:-3]}-t.txt'
        d = 10
    else:
        fn = f'input{__file__[:-3]}.txt'
        d = 140
    file1 = open(fn, 'r+')
    arrt = file1.readlines()
    ret = 0
    arr = np.chararray((1, d))
    arr[:] = 'a'
    for line in arrt:
        line = line.strip()
        arr = np.vstack((arr, list(line)))
    arr = arr[1:]
    for i in range(len(arr)):
        for j in range(len(arr[i])):
                ret += check_diagonal(arr, i, j)
    print(ret)

if __name__ == '__main__':
    part1()
    part2()
