import re  # search, findall, replace
from collections import defaultdict, deque, Counter, OrderedDict
import heapq
import bisect
from itertools import combinations, combinations_with_replacement, permutations, product
import math

grid = [line.strip() for line in open("./input.txt", "r").readlines()]
# grid = [line.strip() for line in open("./test.txt", "r").readlines()]

end = (0, 0)

for y, line in enumerate(grid):
    if line.find("E") != -1:
        end = (line.index("E"), y)

part1 = 0
part2 = float("inf")

for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] in ("a", "S"):
            Q = deque()
            Q.append((j, i, 0))
            visited = set([(j, i)])

            while len(Q) > 0:
                node = Q.popleft()
                x, y, dist = node
                if (x, y) == end:
                    if grid[i][j] == "S":
                        part1 = dist
                    part2 = min(part2, dist)
                    break
                for dx, dy in [(1, 0), (0, -1), (-1, 0), (0, 1)]:
                    nx = x + dx
                    ny = y + dy
                    in_grid = 0 <= nx < len(grid[0]) and 0 <= ny < len(grid)
                    if not in_grid:
                        continue
                    currH = ord(grid[y][x]) if grid[y][x] != "S" else ord("a")
                    nextH = ord(grid[ny][nx]) if grid[ny][nx] != "E" else ord("z")
                    if (nx, ny) not in visited and nextH <= currH + 1:
                        visited.add((nx, ny))
                        Q.append((nx, ny, dist + 1))

print(part1)
print(part2)
