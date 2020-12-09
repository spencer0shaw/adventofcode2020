lines = []
with open("data.txt") as file:
    temp_line = file.readlines()
    for line in temp_line:
        lines.append(int(line.rstrip("\n")))
print(lines)
sums = set()
file_length = len(lines)

for i, x in enumerate(lines):
    valid = x in sums or i < 25
    if not valid:
        print(x)
        break
    for j in range(file_length):
        sums.add(x + lines[j])