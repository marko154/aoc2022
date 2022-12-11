curl https://adventofcode.com/2022/day/DAY/input --cookie "session=SESSION" > file.txt

useful things

import re # search, findall, replace
from collections import defaultdict, deque, Counter, OrderedDict
import heapq
import bisect
from itertools import combinations, combinations_with_replacement, permutations, product
import math

lines = [line.strip() for line in open("./input.txt", "r").readlines()]
