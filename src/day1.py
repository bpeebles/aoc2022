from collections import Counter, defaultdict

sample = \
"""1000
2000
3000

4000

5000
6000

7000
8000
9000

10000"""


def get_rows(src):
    if not src:
        data = sample
    else:
        data = open(src, "r").read()
    rows = [d.strip() for d in data.split("\n")]

    return rows

def get_elves(src):
    rows = get_rows(src)
    elves = defaultdict(int)
    elf = 0
    for line in rows:
        if not line:
            elf += 1
        else:
            elves[elf] += int(line)
    c = Counter(elves)
    return c


def part1(src):
    elves = get_elves(src)
    print(elves.most_common(1)[0][1])


def part2(src):
    elves = get_elves(src)
    print(sum(item[1] for item in elves.most_common(3)))
