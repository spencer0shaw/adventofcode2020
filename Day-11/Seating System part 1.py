lines = []
with open("data.txt") as f:
    for line in f.readlines():
        lines.append(line.rstrip())


def eight_neighs_bounded(y, x, rmin, rmax, cmin, cmax):
    neighs = []

    up = y > rmin
    down = y < rmax
    left = x > cmin
    right = x < cmax

    if up:
        neighs.append([y - 1, x])
        if left:
            neighs.append([y - 1, x - 1])
        if right:
            neighs.append([y - 1, x + 1])
    if down:
        neighs.append([y + 1, x])
        if left:
            neighs.append([y + 1, x - 1])
        if right:
            neighs.append([y + 1, x + 1])
    if left:
        neighs.append([y, x - 1])
    if right:
        neighs.append([y, x + 1])

    return neighs


column_num = len(lines)
row_num = len(lines[0])
while True:
    changed = False
    newlines = [list(temp_line) for temp_line in lines]

    for y in range(column_num):
        for x in range(row_num):
            c = lines[y][x]

            if c == '.':
                continue

            occupied = 0

            for dy, dx in eight_neighs_bounded(y, x, 0, column_num - 1, 0, row_num - 1):
                if lines[dy][dx] == '#':
                    occupied += 1

            if c == 'L' and occupied == 0:
                newlines[y][x] = '#'
                changed = True
            if c == '#' and occupied >= 4:
                newlines[y][x] = 'L'
                changed = True

    if not changed:
        break

    lines = newlines
print(sum(sum(c == '#' for c in row) for row in lines))
