with open("data.txt") as file:
    lines = [line.strip() for line in file]
inputs = []
for line in lines:
    sp, sp1 = line.split(" ")[0], line.split(" ")[1]
    inputs.append([sp, int(sp1)])


def solve(inputs):
    run = set()
    acc = 0
    pos = 0

    while pos not in run:
        inst, val = inputs[pos]
        run.add(pos)

        if inst == 'acc':
            acc += val
            pos += 1
        elif inst == 'jmp':
            pos += val
        elif inst == 'nop':
            pos += 1
    return acc


print(solve(inputs))
