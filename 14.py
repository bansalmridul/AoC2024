import os, time
import numpy as np


def extract_pos(line, time=100):
    halves = line.split(" ")
    arr_p = halves[0].split("=")[1].split(",")
    arr_v = halves[1].split("=")[1].split(",")
    # print(arr_p, arr_v)
    return (
        int(arr_p[0]) + time * int(arr_v[0]),
        int(arr_p[1]) + time * int(arr_v[1]),
    )


def extract_pos2(line, time=100):
    halves = line.split(" ")
    arr_p = halves[0].split("=")[1].split(",")
    arr_v = halves[1].split("=")[1].split(",")
    # print(arr_p, arr_v)
    return int(arr_p[0]), int(arr_p[1]), int(arr_v[0]), int(arr_v[1])


def part1(test=False):
    fn = os.path.basename(__file__)

    dim_x, dim_y = 101, 103
    if test:
        fn = f"input{fn[:-3]}-t.txt"
        dim_x, dim_y = 11, 7
    else:
        fn = f"input{fn[:-3]}.txt"
    file1 = open(fn, "r+")
    lines = file1.readlines()
    ret = 0
    quadrants = [0] * 4
    for line in lines:
        x, y = extract_pos(line)
        x %= dim_x
        y %= dim_y
        # print(x, y)
        if x == dim_x // 2 or y == dim_y // 2:
            continue
        quadrants[2 * (x < dim_x // 2) + (y < dim_y // 2)] += 1
    print(quadrants[0] * quadrants[1] * quadrants[2] * quadrants[3])


def print_array_as_dots(array):
    if array[0][0] == 255:
        array = 1 - array / 255
    for row in array:
        print("".join("⬛" if val < 0.5 else "⬜" for val in row))


def part2(test=False):
    fn = os.path.basename(__file__)
    dim_x, dim_y = 101, 103
    if test:
        fn = f"input{fn[:-3]}-t.txt"
        dim_x, dim_y = 11, 7
    else:
        fn = f"input{fn[:-3]}.txt"
    file1 = open(fn, "r+")
    lines = file1.readlines()
    arr = np.zeros((dim_x, dim_y), dtype=int)
    point_list = []

    inc = 8050
    for line in lines:
        x, y, px, py = extract_pos2(line)
        nx, ny = (x + inc * px) % dim_x, (y + inc * py) % dim_y
        point_list.append((nx, ny, px, py))
        arr[nx][ny] += 1
    count = inc
    max_score = 0
    while True:
        print_array_as_dots(np.transpose(arr))
        print(count)
        time.sleep(0.5)
        for i in range(len(point_list)):
            x, y = point_list[i][0], point_list[i][1]
            vx, vy = point_list[i][2], point_list[i][3]
            nx, ny = (x + vx) % dim_x, (y + vy) % dim_y
            arr[x][y] -= 1
            arr[nx][ny] += 1
            point_list[i] = (nx, ny, vx, vy)
        count += 1


def main():
    t = time.perf_counter()
    part1()
    t1 = time.perf_counter()
    print(f"Time 1: {t1 - t}")
    part2()


if __name__ == "__main__":
    main()
