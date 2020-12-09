with open("data.txt") as file:
    lines = [line.strip() for line in file]
inputs = []
for line in lines:
    sp, sp1 = line.split(" ")[0], line.split(" ")[1]
    inputs.append([sp, int(sp1)])


def solve(line_input):
    jmp_pop = [x for x in range(len(line_input)) if line_input[x][0] == 'jmp']
    nop_pop = [x for x in range(len(line_input)) if line_input[x][0] == 'nop']

    changes = [[x, 'nop'] for x in jmp_pop] + [[x, 'jmp'] for x in nop_pop]

    for change_pos, change in changes:
        new_program = list(list(row) for row in line_input)
        new_program[change_pos][0] = change

        run = set()
        acc, pos = 0, 0

        while pos not in run:
            if pos == len(line_input):
                return acc

            inst, val = new_program[pos]
            run.add(pos)

            if inst == 'acc':
                acc += val
                pos += 1
            elif inst == 'jmp':
                pos += val
            elif inst == 'nop':
                pos += 1


print(solve(inputs))
