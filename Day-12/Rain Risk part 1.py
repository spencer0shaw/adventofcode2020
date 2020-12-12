def rotate(facing, steps):
    if steps == 0:
        return facing

    if steps < 0:
        return rotate(facing, 4 + steps)

    if facing == [0, 1]:
        return rotate([-1, 0], steps - 1)
    if facing == [-1, 0]:
        return rotate([0, -1], steps - 1)
    if facing == [0, -1]:
        return rotate([1, 0], steps - 1)

    return rotate([0, 1], steps - 1)


lines = []

with open("data.txt") as f:
    for line in f.readlines():
        lines.append(line.strip())

facing = [0, 1]
y = 0
x = 0

for instruction in lines:
    command = instruction[0]
    val = int(instruction[1:])

    if command == 'N':
        y += val
    if command == 'S':
        y -= val
    if command == 'E':
        x += val
    if command == 'W':
        x -= val
    if command == 'L':
        if val == 90:
            facing = rotate(facing, -1)
        if val == 180:
            facing = rotate(facing, -2)
        if val == 270:
            facing = rotate(facing, -3)
    if command == 'R':
        if val == 90:
            facing = rotate(facing, 1)
        if val == 180:
            facing = rotate(facing, 2)
        if val == 270:
            facing = rotate(facing, 3)
    if command == 'F':
        y += val * facing[0]
        x += val * facing[1]


def manhattan(a, b):
    return sum([abs(a[x] - b[x]) for x in range(len(a))])


print(manhattan((y, x), (0, 0)))
