lines = []
with open("data.txt", encoding="utf-8") as f:
    for line in f.readlines():
        if line is not None:
            lines.append(line.strip("\n"))
trees0, trees1, trees2, trees3, trees4 = 0, 0, 0, 0, 0
path0, path1, path2, path3, path4 = 1, 1, 1, 1, 1

i = 0
for maps in lines:
    maps0, maps1, maps2, maps3, maps4 = maps, maps, maps, maps, maps
    if path0 > len(maps):
        times = path0 // len(maps) + 1
        maps0 = maps * times
    if maps0[path0-1] == "#":
        trees0 += 1
    path0 += 1

    if path1 > len(maps):
        times = path1 // len(maps) + 1
        maps1 = maps * times
    if maps1[path1-1] == "#":
        trees1 += 1
    path1 += 3

    if path2 > len(maps):
        times = path2 // len(maps) + 1
        maps2 = maps * times
    if maps2[path2-1] == "#":
        trees2 += 1
    path2 += 5

    if path3 > len(maps):
        times = path3 // len(maps) + 1
        maps3 = maps * times
    if maps3[path3-1] == "#":
        trees3 += 1
    path3 += 7

    if i % 2 == 0:
        if path4 > len(maps):
            times = path4 // len(maps) + 1
            maps4 = maps * times
        if maps4[path4-1] == "#":
            trees4 += 1
        path4 += 1

    i += 1
print(trees0 * trees1 * trees2 * trees3 * trees4)
