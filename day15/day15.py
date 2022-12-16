import re

lines = [line.strip() for line in open("./input.txt", "r").readlines()]

y = 200000

pairs = set()

for line in lines:
    sx, sy, bx, by = [int(x) for x in re.findall(r"[0-9]+", line)]

    pairs.add(((sx, sy), (bx, by)))

ans = 0

for x in range(0, 10000000):
    for sensor, beacon in pairs:
        sx, sy = sensor
        bx, by = beacon
        dist = abs(sx - bx) + abs(sy - by)
        cdist = abs(sx - x) + abs(sy - y)
        if cdist <= dist:
            ans += 1

print(ans)
