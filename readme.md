curl https://adventofcode.com/2022/day/DAY/input --cookie "session=SESSION" > input.txt

template

```py
import re # search, findall, replace
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
```
