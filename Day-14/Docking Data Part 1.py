import re

lines = []
with open("data.txt") as f:
    for line in f.readlines():
        lines.append(line.strip())

mem = {}
mask = ''
for element in lines:
    if element.startswith('mask'):
        mask = element.split(' = ')[1]
    else:
        pattern = r'^mem\[(?P<address>\d*)\] = (?P<value>.*)'
        m = re.match(pattern, element)
        address = int(m['address'])
        value = int(m['value'])
        for i, bit in [(i, int(x)) for i, x in enumerate(mask[::-1]) if x != 'X']:
            if bit:
                value = value | (1 << i)
            else:
                value = value & ~(1 << i)
        mem[address] = mem.get(address, 0)
        mem[address] = value
print(sum(mem.values()))