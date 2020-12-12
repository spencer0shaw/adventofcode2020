lines = []

with open('data.txt') as f:
    for line in f.readlines():
        lines.append(line.strip())

wayy = 1
wayx = 10
y = 0
x = 0

for instruction in lines:
    command = instruction[0]
    val = int(instruction[1:])

    if command == 'N':
        wayy += val
    if command == 'S':
        wayy -= val
    if command == 'E':
        wayx += val
    if command == 'W':
        wayx -= val
    if command == 'L':
        if val == 90:
            wayy, wayx = wayx, wayy * -1
        if val == 180:
            wayy, wayx = wayy * -1, wayx * -1
        if val == 270:
            wayy, wayx = wayx * -1, wayy
    if command == 'R':
        if val == 90:
            wayy, wayx = wayx * -1, wayy
        if val == 180:
            wayy, wayx = wayy * -1, wayx * -1
        if val == 270:
            wayy, wayx = wayx, wayy * -1
    if command == 'F':
        y += val * wayy
        x += val * wayx


def manhattan(a, b):
    return sum([abs(a[x] - b[x]) for x in range(len(a))])


print(manhattan((y, x), (0, 0)))
