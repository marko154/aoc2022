import re
import heapq
from collections import deque
import sys

sys.setrecursionlimit(1000000)

lines = [line.strip() for line in open("./input.txt", "r").readlines()]
lines = [line.strip() for line in open("./test.txt", "r").readlines()]

valves = {}

for line in lines:
    v, *exits = re.findall(r"[A-Z][A-Z]", line)
    rate = int(re.findall(r"\-?\d+", line)[0])

    valves[v] = [rate, exits]

print(valves)
ans = 0


for i, valve in enumerate(valves):
    rate, exits = valves[valve]
    seen = set()
    if valve != "DD":
        continue

    def dfs(valve, time):
        global seen, valves
        rate, exits = valves[valve]
        if rate != 0:
            time -= 2
        pressure = time * rate

        max_pressure = 0

        for exit in exits:
            if exit not in seen:
                seen.add(valve)
                with_ = dfs(exit, time - 2)
                seen.remove(valve)
                wihtout = dfs(exit, time - 1)
                max_pressure = max(max_pressure, with_, wihtout)
                print(valve, exit, with_, wihtout)
        if max_pressure == 0:
            print("end", time, valve)
        return pressure + max_pressure

    time = 31 if i == 0 else 30
    best_pressure = dfs(valve, time)
    print(best_pressure)
    ans = max(ans, best_pressure)

print(ans)
