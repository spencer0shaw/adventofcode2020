lines = []
with open("data.txt") as f:
    for line in f.readlines():
        lines.append(line.strip())

lines.append('0')
s = map(lambda a: int(a.strip()), lines)
ss = sorted(s)
threes = 1
ones = 0

for i in range(len(ss) - 1):
    if ss[i + 1] - ss[i] == 1:
        ones += 1
    elif ss[i + 1] - ss[i] == 3:
        threes += 1
print(threes, ones, threes * ones)
