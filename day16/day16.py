import matplotlib.pyplot as plt
import networkx as nx
import re

lines = [line.strip() for line in open("./input.txt", "r").readlines()]
# lines = [line.strip() for line in open("./test.txt", "r").readlines()]

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
            matrix[fr][to] = min(matrix[fr][to], matrix[fr][via] + matrix[via][to])

opened = set()
DP = {}

nodes = [i for i in range(len(matrix)) if valves[i][0] == "AA" or valves[i][1] > 0]


def dfs(valve, time):
    global opened, valves, nodes
    if time <= 0 or len(opened) == len(nodes) - 1:
        return 0
    name, rate, _ = valves[valve]
    key = (time, valve, *tuple(sorted(opened)))
    if key in DP:
        return DP[key]
    max_pressure = 0

    for exit in nodes:
        dist = matrix[valve][exit]
        if exit == valve or dist == float("inf"):
            continue

        without = dfs(exit, time - dist)
        max_pressure = max(max_pressure, without)
        # if already open dont open again

        if valve not in opened and rate != 0:
            opened.add(valve)
            with_ = dfs(exit, time - dist - 1)
            max_pressure = max(max_pressure, with_ + time * rate)
            if valve in opened:
                opened.remove(valve)
    DP[key] = max_pressure
    return max_pressure


best_pressure = dfs(mapping["AA"], 29)
print(best_pressure)


# G = nx.DiGraph()


# for node in nodes:
#     for inode in nodes:
#         dist = matrix[node][inode]
#         if inode == node or dist > 9999999:
#             continue
#         G.add_edge(
#             valves[node][0] + str(valves[node][1]),
#             valves[inode][0] + str(valves[node][1]),
#             weight=dist,
#         )

# pos = nx.get_node_attributes(G, "pos")
# pos = nx.spring_layout(G)  # pos = nx.nx_agraph.graphviz_layout(G)
# nx.draw_networkx(G, pos)
# # labels = nx.get_edge_attributes(G, "weight")
# # nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
# plt.show()
