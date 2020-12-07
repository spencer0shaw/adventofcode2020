lines = []
with open("data.txt", encoding="utf-8") as f:
    for line in f.readlines():
        if line is not None:
            lines.append(line.strip("\n"))
right = 0
for password in lines:
    num1 = password.partition("-")[0]
    temp1 = password.partition("-")[2]
    num2 = temp1.partition(" ")[0]
    temp2 = temp1.partition(" ")[2]
    letter = temp2.partition(":")[0]
    save = temp2.partition(" ")[2]

    if save[int(num1)-1] == letter and save[int(num2)-1] == letter:
        continue
    elif save[int(num1)-1] != letter and save[int(num2)-1] != letter:
        continue
    else:
        right += 1

print(right)