import re  # search, findall, replace
from collections import defaultdict, deque, Counter, OrderedDict
from sortedcontainers import SortedDict, SortedSet, SortedList
import heapq
import bisect
from itertools import combinations, combinations_with_replacement, permutations, product
import math
import numpy as np
import sys

filename = "./input.txt" if len(sys.argv) < 2 else sys.argv[1]
grid, dirs = open(filename, "r").read().split("\n\n")
grid = grid.splitlines()

points = {}

for i, row in enumerate(grid):
    for j, cell in enumerate(grid):
        if cell in (".", "#"):
            data = [cell]

            # left
            lj = (j - 1) % len(row)
            while grid[i][lj] == " ":
                lj = (j - 1) % len(row)
            rj = (j + 1) % len(row)
            while grid[i][rj] == " ":
                rj = (j + 1) % len(row)
            data.append((i, rj))
            points[(i, j)] = data


pos = (0, 0)
dir = (1, 0)

print(grid)
print(dirs)
