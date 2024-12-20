import os, time


def iterate_program(register, program):
    def instruction(opcode, operand, k):
        if opcode in [0, 2, 5, 6, 7] and operand >= 4:
            operand = register[operand - 4]
            if operand == 7:  # failsafe
                return -10
        if opcode == 0:
            register[0] = register[0] // (1 << operand)
        elif opcode == 1:
            register[1] = register[1] ^ operand
        elif opcode == 2:
            register[1] = operand % 8
        elif opcode == 3 and register[0] != 0:
            return operand - 2
        elif opcode == 4:
            register[1] = register[1] ^ register[2]
        elif opcode == 5:
            print(operand % 8, end=",")
        elif opcode == 6:
            register[1] = register[0] // (1 << operand)
        elif opcode == 7:
            register[2] = register[0] // (1 << operand)
        return k

    i = 0
    while 0 <= i < len(program):
        opcode = program[i]
        operand = program[i + 1]
        i = instruction(opcode, operand, i) + 2


def part1and2(test=False):
    fn = os.path.basename(__file__)
    if test:
        fn = f"input{fn[:-3]}-t.txt"
    else:
        fn = f"input{fn[:-3]}.txt"
    file1 = open(fn, "r+")
    lines = file1.readlines()
    register_init = [int(lines[0].split(":")[1]), int(lines[1].split(":")[1]), int(lines[2].split(":")[1])]
    program = [int(x) for x in lines[4].split(":")[1].split(",")]

    iterate_program(register_init, program)
    print()

    program.reverse()
    c_set = {0}
    for goal in program:
        # print(i, end=': ')
        n_set = set()
        for curr in c_set:
            for d in range(8):
                x = 8 * curr + d
                B = 5 ^ (x % 8)
                out = (6 ^ (x >> B) ^ B) % 8  # hardcoded but whatev
                if out == goal:
                    n_set.add(x)
        c_set = n_set
    print(min(c_set))


def main():
    t = time.perf_counter()
    part1and2()
    print(f"Time: {time.perf_counter() - t}")


if __name__ == "__main__":
    main()
