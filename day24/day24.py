from collections import defaultdict, deque
import sys
import math

filename = "./input.txt" if len(sys.argv) < 2 else sys.argv[1]
lines = [line.strip() for line in open(filename, "r").readlines()]

blizzards = defaultdict(list)
dirs = ((-1, 0), (0, 1), (1, 0), (0, -1))
arrows = "^>v<"

for i, line in enumerate(lines):
    for j, cell in enumerate(line):
        if cell in arrows:
            blizzards[(i, j)].append(dirs[arrows.index(cell)])

H = len(lines)
W = len(lines[0])
looped = (H - 2) * (W - 2) // math.gcd((H - 2), (W - 2))

blizzards_at_time = {}

for time in range(looped):
    next_blizzards = set()
    for bi, bj in blizzards:
        for di, dj in blizzards[(bi, bj)]:
            ni = 1 + (bi - 1 + di * time) % (H - 2)
            nj = 1 + (bj - 1 + dj * time) % (W - 2)
            next_blizzards.add((ni, nj))
    blizzards_at_time[time] = next_blizzards

start = (0, 1)
end = (H - 1, W - 2)


def shortest_path(start_time, start, end):
    seen = set([(*start, start_time)])
    Q = deque([(*start, start_time)])

    while Q:
        i, j, time = Q.popleft()
        if (i, j) == end:
            return time
        next_time = (time + 1) % looped
        next_blizzards = blizzards_at_time[next_time]

        for di, dj in [*dirs, (0, 0)]:
            ni, nj = (i + di, j + dj)
            is_not_wall = 0 < ni < H - 1 and 0 < nj < W - 1 or (ni, nj) in (start, end)
            if (
                (ni, nj, next_time) not in seen
                and (ni, nj) not in next_blizzards
                and is_not_wall
            ):
                Q.append((ni, nj, time + 1))
                seen.add((ni, nj, next_time))


end_time = shortest_path(0, start, end)
print(end_time)
return_time = shortest_path(end_time, end, start)
print(shortest_path(return_time, start, end))
