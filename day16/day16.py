# import matplotlib.pyplot as plt
# import networkx as nx
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


def dfs(my_state, elephant_state):
    global opened, valves, nodes
    me, my_time = my_state
    elephant, elephant_time = elephant_state
    if min(my_time, elephant_time) <= 0:
        return 0
    _, my_rate, _ = valves[me]
    _, elephant_rate, _ = valves[elephant]

    # DP
    tupled = tuple(sorted(opened))
    key = (my_time, elephant_time, me, elephant, *tupled)
    symmetric_key = (elephant_time, my_time, elephant, me, *tupled)
    if key in DP:
        return DP[key]
    if symmetric_key in DP:
        return DP[symmetric_key]

    max_pressure = 0
    # cases
    # i open, elephant doesnt
    # i open elephant does
    # i dont open elephant doesnt
    # i dont open elephant does
    # check if me and elephant are in the same position before

    # print(my_time, elephant_time)
    assert my_time > 0
    assert elephant_time > 0

    for my_exit in nodes:
        my_dist = matrix[me][my_exit]
        if my_exit == me or my_dist == float("inf"):
            continue
        for elephant_exit in nodes:
            elephant_dist = matrix[elephant][elephant_exit]
            if elephant_exit == elephant or elephant_dist == float("inf"):
                continue
            without = dfs(
                (my_exit, my_time - my_dist),
                (elephant_exit, elephant_time - elephant_dist),
            )
            max_pressure = max(max_pressure, without)
            if elephant not in opened and elephant_rate != 0:
                opened.add(elephant)
                with_elephant = dfs(
                    (my_exit, my_time - my_dist),
                    (elephant_exit, elephant_time - elephant_dist - 1),
                )
                max_pressure = max(
                    max_pressure, with_elephant + elephant_rate * elephant_time
                )
                opened.discard(elephant)
        if me not in opened and my_rate != 0 and me != elephant:
            opened.add(me)
            for elephant_exit in nodes:
                elephant_dist = matrix[elephant][elephant_exit]
                if (
                    elephant in opened
                    or elephant_exit == elephant
                    or elephant_dist == float("inf")
                ):
                    continue
                opened.add(elephant)
                with_both = dfs(
                    (my_exit, my_time - my_dist - 1),
                    (elephant_exit, elephant_time - elephant_dist - 1),
                )
                max_pressure = max(
                    max_pressure,
                    with_both + elephant_rate * elephant_time + my_rate * my_time,
                )
                opened.discard(elephant)
            opened.discard(me)

    DP[key] = max_pressure
    return max_pressure


start = (mapping["AA"], 25)
best_pressure = dfs(start, start)
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
