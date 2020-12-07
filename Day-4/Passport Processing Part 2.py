import re
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
# print(lines)
list = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

correct = 0
correct_list = []
detail_list = []
for info in lines:
    if all(f in info for f in list):
        correct_list.append(info)
for element in correct_list:
    details = element.split(" ")
    detail_list.append(details)

eye_list = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
for element in detail_list:
    byr, iyr, eyr, hgt, hcl, ecl, pid = "", "", "", "", "", "", ""
    tr = 0
    for x in element:
        if x[0:4] == 'byr:':
            byr = x[4:]
            if int(byr) in range(1920, 2003):
                tr += 1
        elif x[0:4] == "iyr:":
            iyr = x[4:]
            if int(iyr) in range(2010, 2021):
                tr += 1
        elif x[0:4] == "eyr:":
            eyr = x[4:]
            if int(eyr) in range(2020, 2031):
                tr += 1
        elif x[0:4] == "hgt:":
            hgt = x[4:-2]
            title = x[-2:]
            if title == "cm":
                if int(hgt) in range(150, 194):
                    tr += 1
            elif title == "in":
                if int(hgt) in range(59, 77):
                    tr += 1
        elif x[0:4] == "hcl:":
            hcl = x[4:]
            if hcl[0:1] == "#" and len(hcl) == 7:
                temp_hcl = x[5:]
                if re.match("^[0-9a-f]", temp_hcl):
                    tr += 1
        elif x[0:4] == "ecl:":
            ecl = x[4:]
            if any(f in ecl for f in eye_list):
                tr += 1
        elif x[0:4] == "pid:":
            pid = x[4:]
            if pid.isnumeric() and len(pid) == 9:
                tr += 1

    if tr == 7:
        correct += 1
print(correct)