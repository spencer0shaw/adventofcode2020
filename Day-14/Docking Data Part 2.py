import re
from itertools import product

lines = []
with open("data.txt") as f:
    for line in f.readlines():
        lines.append(line.strip())


def get_addresses(addr, mask_input):
    address_bin = format(addr, '036b')
    res = ''.join(['X' if x == 'X' or y == 'X' else str(int(x) | int(y)) for x, y in zip(address_bin, mask_input)])
    count_x = mask_input.count('X')
    ret = []
    for c in product(range(2), repeat=count_x):
        perm = res.replace('X', '{}').format(*c)
        ret.append(perm)
    return ret


mem = {}
mask = ''
for element in lines:
    if element.startswith('mask'):
        mask = element.split(' = ')[1]
    else:
        pattern = r'^mem\[(?P<address>\d*)\] = (?P<value>.*)'
        match = re.match(pattern, element)
        address = int(match['address'])
        value = int(match['value'])
        for a in get_addresses(address, mask):
            mem[a] = mem.get(a, 0)
            mem[a] = value

print(sum(mem.values()))
