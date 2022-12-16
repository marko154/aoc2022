import matplotlib.pyplot as plt
import networkx as nx
import re

lines = [line.strip() for line in open("./input.txt", "r").readlines()]
lines = [line.strip() for line in open("./test.txt", "r").readlines()]

valves = [0] * len(lines)
matrix = [[float("inf")] * len(lines) for x in range(len(lines))]
mapping = {}
i = 0

for line in lines:
    v, *exits = re.findall(r"[A-Z][A-Z]", line)
    if v not in mapping:
        mapping[v] = i
        i += 1
    for exit in exits:
        if exit not in mapping:
            mapping[exit] = i
            i += 1
        matrix[mapping[v]][mapping[exit]] = 1
    rate = int(re.findall(r"\-?\d+", line)[0])
    valves[v] = [rate, exits]

edges = []

for valve in valves:
    rate, exits = valves[valve]
    for exit in exits:
        rate2, _ = valves[exit]
        edges.append((valve + str(rate), exit + str(rate2)))


for valve in valves:
    index = valve
    for
    matrix[]

G = nx.DiGraph()
G.add_edges_from(edges)
nx.draw_networkx(G)
plt.show()
exit()

ans = 0

opened = set()
DP = {}
print(valves)


def dfs(valve, time):
    global opened, valves
    if time <= 0:
        return 0
    rate, exits = valves[valve]
    tupled = tuple(sorted(opened))
    if (valve, time, *tupled) in DP:
        return DP[(valve, time, *tupled)]
    max_pressure = 0

    for exit in exits:
        without = dfs(exit, time - 1)
        max_pressure = max(max_pressure, without)
        # if already open dont open again
        if valve not in opened or rate == 0:
            opened.add(valve)
            with_ = dfs(exit, time - 2)
            max_pressure = max(max_pressure, with_ + time * rate)
            if valve in opened:
                opened.remove(valve)
    DP[(valve, time, *tupled)] = max_pressure
    return max_pressure


best_pressure = dfs("AA", 29)
ans = max(ans, best_pressure)

print(ans)
