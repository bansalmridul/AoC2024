import math
import os, re

def extract_numbers(string):
  pattern = r"X[+=](\d+), Y[+=](\d+)"
  matches = re.findall(pattern, string)
  x_num, y_num = map(int, matches[0])
  return x_num, y_num

def minCost(Ax, Ay, Bx, By, Px, Py):
    coeff_det = Ax*By - Bx * Ay
    if coeff_det == 0 and px % gcd(ax, bx) != 0:
        print("oogly boogly")
        return 0
    m_det = Px*By - Bx * Py
    n_det = Ax*Py - Px * Ay
    if m_det % coeff_det != 0:
        return 0
    if n_det % coeff_det != 0:
        return 0
    m = m_det //coeff_det
    n = n_det // coeff_det
    return 3 * m + n

def part1and2(test=False):
    fn = os.path.basename(__file__)
    if test:
        fn = f"input{fn[:-3]}-t.txt"
    else:
        fn = f"input{fn[:-3]}.txt"
    file1 = open(fn, "r+")
    lines = file1.readlines()
    ret1 = 0
    ret2 = 0
    for i in range(0, len(lines), 4):
        Ax, Ay = extract_numbers(lines[i])
        Bx, By = extract_numbers(lines[i+1])
        Px, Py = extract_numbers(lines[i+2])
        ret1 += minCost(Ax, Ay, Bx, By, Px, Py)
        ret2 += minCost(Ax, Ay, Bx, By, Px + 10000000000000, Py + 10000000000000)
    print(ret1)
    print(ret2)


if __name__ == "__main__":
    part1and2()
    #part2()
