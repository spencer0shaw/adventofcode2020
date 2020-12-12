lines = []
with open("data.txt") as f:
    for line in f.readlines():
        lines.append(line.rstrip())


def eight_neighs(y, x):
    return [[y - 1, x - 1], [y - 1, x], [y - 1, x + 1], [y + 1, x - 1], [y + 1, x], [y, x - 1], [y + 1, x + 1],
            [y, x + 1]]


column_num = len(lines)
row_num = len(lines[0])

while True:
    changed = False

    newlines = [list(line) for line in lines]

    for y in range(column_num):
        for x in range(row_num):
            c = lines[y][x]

            if c == '.':
                continue

            occupied = 0

            dirs = eight_neighs(0, 0)

            for dy, dx in dirs:
                diry = dy
                dirx = dx

                while 0 <= y + diry < column_num and 0 <= x + dirx < row_num:
                    if lines[y + diry][x + dirx] in 'L#':
                        if lines[y + diry][x + dirx] == '#':
                            occupied += 1
                        break

                    diry += dy
                    dirx += dx

            if c == 'L' and occupied == 0:
                newlines[y][x] = '#'
                changed = True
            if c == '#' and occupied >= 5:
                newlines[y][x] = 'L'
                changed = True

    if not changed:
        break

    lines = newlines

print(sum(sum(c == '#' for c in row) for row in lines))
