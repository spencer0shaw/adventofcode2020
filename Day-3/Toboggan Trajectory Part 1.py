lines = []
with open("data.txt", encoding="utf-8") as f:
    for line in f.readlines():
        if line is not None:
            lines.append(line.strip("\n"))
trees = 0
path = 1

for maps in lines:
    if path > len(maps):
        times = path // len(maps) + 1
        maps = maps * times
    if maps[path-1] == "#":
        trees += 1
    path += 7
print(trees)
