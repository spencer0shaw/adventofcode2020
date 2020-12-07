lines = []
file = open("data.txt")
temp = ""
i = 0

file_line = file.readlines()
length = len(file_line)


for line in file_line:
    i += 1
    if line != "\n":
        temp += line.strip("\n") + " "
        if i == length:
            lines.append(temp[:-1])
    elif i == length and temp is not None:
        lines.append(temp[:-1])
    else:
        lines.append(temp[:-1])
        temp = ""

list = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

correct = 0
for info in lines:
    if all(f in info for f in list):
        correct += 1
print(correct)
