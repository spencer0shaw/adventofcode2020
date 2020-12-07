lines = []
with open("data1.txt", encoding="utf-8") as f:
    for line in f.readlines():
        if line is not None:
            lines.append(line.strip("\n"))

for i in range(0, len(lines)):
    num1 = lines[i]
    for j in range(i + 1, len(lines)):
        num2 = lines[j]
        if int(num1) + int(num2) == 2020:
            print("in")
            print(int(num1) * int(num2))
