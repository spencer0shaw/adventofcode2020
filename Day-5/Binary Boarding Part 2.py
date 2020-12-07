file = open("data.txt")
file_line = file.readlines()
position = []
row_list = []
column_list = []
ticket_num_list = []
for line in file_line:
    temp_lines_list = []
    temp_lines = line[:-1]
    temp_lines = temp_lines.replace("F", "0")
    temp_lines = temp_lines.replace("B", "1")
    temp_lines = temp_lines.replace("L", "0")
    temp_lines = temp_lines.replace("R", "1")
    row_num = int(temp_lines[0:7], 2)
    column_num = int(temp_lines[7:], 2)
    ticket_num = int(temp_lines[0:7], 2) * 8 + int(temp_lines[7:], 2)
    row_list.append(row_num)
    column_list.append(column_num)
    ticket_num_list.append(ticket_num)
    temp_lines_list.append(row_num)
    temp_lines_list.append(column_num)
    position.append(temp_lines_list)

min = min(ticket_num_list)
max = max(ticket_num_list)

j = 0
for j in range(min, max):
    if j not in ticket_num_list and j != 255:
        print(j)
