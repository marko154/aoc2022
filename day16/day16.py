import matplotlib.pyplot as plt
import networkx as nx
import re
import time as Time
from itertools import permutations

lines = [line.strip() for line in open("./input.txt", "r").readlines()]
lines = [line.strip() for line in open("./test.txt", "r").readlines()]

valves = [[]] * len(lines)
matrix = [[float("inf")] * len(lines) for x in range(len(lines))]
mapping = {}
i = 0

for line in lines:
    v, *exits = re.findall(r"[A-Z][A-Z]", line)
    rate = int(re.findall(r"\d+", line)[0])
    if v not in mapping:
        mapping[v] = i
        i += 1
    for exit in exits:
        if exit not in mapping:
            mapping[exit] = i
            i += 1
        matrix[mapping[v]][mapping[exit]] = 1
    valves[mapping[v]] = [v, rate, exits]

for via in range(len(matrix)):
    for fr in range(len(matrix)):
        for to in range(len(matrix)):
            matrix[fr][to] = min(matrix[fr][to], matrix[fr]
                                 [via] + matrix[via][to])


# nodes = [i for i in range(len(matrix)) if valves[i][1] > 0]

# best = 0
# for permutation in permutations(nodes):
#     score = 0
#     time = 30
#     valve = mapping["AA"]
#     for node in permutation:
#         time -= matrix[valve][node] + 1
#         score += time * valves[node][1]
#         valve = node
#     best = max(best, score)

# print(best)

visited = set()
DP = {}

nodes = [i for i in range(len(matrix)) if valves[i][0]
         == "AA" or valves[i][1] > 0]


def dfs(valve, time):
    global visited, valves, nodes
    if time <= 0:
        return 0
    # key = (valve, time, tuple(sorted(visited)))
    # if key in DP:
    #     return DP[key]
    name, rate, _ = valves[valve]
    visited.add(valve)
    max_pressure = 0

    for exit in nodes:
        dist = matrix[valve][exit]
        if exit not in visited:
            next_time = time - dist - 1
            pressure = dfs(exit, next_time)
            max_pressure = max(max_pressure, pressure)

    # DP[key] = max_pressure
    visited.discard(valve)
    return max_pressure + time * rate


best_pressure = dfs(mapping["AA"], 30)
print(best_pressure)


# for i, line in enumerate(matrix):
#     if i == 0:
#         print("    ", end="")
#         for j in range(len(matrix)):
#             print(valves[j][0], end=" ")
#         print()
#     print(valves[i][0], end=" ")
#     print(line)

# G = nx.DiGraph()


# for node in nodes:
#     for inode in nodes:
#         dist = matrix[node][inode]
#         if inode == node or dist > 9999999:
#             continue
#         G.add_edge(
#             valves[node][0] + str(valves[node][1]),
#             valves[inode][0] + str(valves[inode][1]),
#             weight=dist,
#         )

# pos = nx.get_node_attributes(G, "pos")
# pos = nx.spring_layout(G)  # pos = nx.nx_agraph.graphviz_layout(G)
# nx.draw_networkx(G, pos)
# labels = nx.get_edge_attributes(G, "weight")
# nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
# plt.show()
