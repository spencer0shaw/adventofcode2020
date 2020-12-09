lines = []
with open("data.txt") as file:
    temp_line = file.readlines()
    for line in temp_line:
        lines.append(int(line.rstrip("\n")))

sums = set()
file_length = len(lines)

for pos, num in enumerate(lines):
    list_sum = num
    for offset, num2 in enumerate(lines[pos+1:]):
        offset += 1
        list_sum += num2

        if list_sum == 14144619:
            min_value = min(lines[pos:offset+pos+1])
            max_value = max(lines[pos:offset+pos+1])

            print(f"tast 2: {min_value+max_value}")
        if list_sum > 14144619:
            break