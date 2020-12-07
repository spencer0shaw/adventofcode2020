import os

lines = []
with open("data1.txt", encoding="utf-8") as f:
    for line in f.readlines():
        if line is not None:
            lines.append(line.strip("\n"))

# print(lines)

for i in range(0, len(lines)):
    num1 = lines[i]
    for j in range(i + 1, len(lines)):
        num2 = lines[j]
        for k in range(i, len(lines)):
            num3 = lines[k]
            if int(num1) + int(num2) + int(num3) == 2020:
                print("in")
                print(int(num1) * int(num2) * int(num3))