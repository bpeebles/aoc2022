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


def run(src):
    if not src:
        data = sample
    else:
        data = open(src, "r").read()
    rows = data.split("\n")

    peak = cur = 0
    for line in rows:
        if not line.strip():
            if cur > peak:
                peak = cur
            cur = 0
        else:
            cur += int(line.strip())
    print(peak)
