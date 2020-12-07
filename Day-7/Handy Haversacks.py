from collections import defaultdict
from functools import reduce

bagdef = {bd[0].rsplit(' ', maxsplit=1)[0]: [
    (lambda l: (int(l[0]), l[1]))(b.rsplit(' ', maxsplit=1)[0].split(' ', maxsplit=1)) for b in bd[1].split(', ') if
    b != 'no other bags'] for bd in (l.rstrip('.\n').split(' contain ') for l in open('data.txt'))}

contdef = defaultdict(set)
for container, contents in bagdef.items():
    for c in contents:
        contdef[c[1]].add(container)


def containers(cd, colour):
    return reduce(set.union, (containers(cd, cc) for cc in cd[colour]), cd[colour])


print(len(containers(contdef, 'shiny gold')))


def contents(bagdef, colour):
    return sum(i + i * contents(bagdef, cc) for i, cc in bagdef[colour])


print(contents(bagdef, 'shiny gold'))
