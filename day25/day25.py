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
lines = [line.strip() for line in open(filename, "r").readlines()]

L = max(len(x) for x in lines)
ctr = [0] * L

for line in lines:
    for i, char in enumerate(line[::-1]):
        if char in "12":
            ctr[i] += int(char)
        elif char == "=":
            ctr[i] -= 2
        elif char == "-":
            ctr[i] -= 1

snafu = ""
for i in range(L):
    n = ctr[i]
    if i + 1 < L:
        ctr[i + 1] += n // 5
    n = n % 5
    if 0 <= n <= 2:
        digit = str(n)
    else:
        ctr[i + 1] += 1
        digit = "=" if n == 3 else "-"
    snafu = digit + snafu

print(snafu)
