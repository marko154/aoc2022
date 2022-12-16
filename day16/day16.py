import re

lines = [line.strip() for line in open("./input.txt", "r").readlines()]

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

nodes = [i for i in range(len(matrix)) if valves[i][0]
         == "AA" or valves[i][1] > 0]
nodes.sort(key=lambda node: valves[node][0])
visited = set()


def dfs(valve, time, nodes, visited):
    global valves
    if time <= 0:
        return 0

    name, rate, _ = valves[valve]
    visited.add(valve)
    max_pressure = 0

    for exit in nodes:
        dist = matrix[valve][exit]
        if exit not in visited:
            pressure = dfs(exit, time - dist - 1, nodes, visited)
            max_pressure = max(max_pressure, pressure)

    visited.discard(valve)
    return max_pressure + time * rate


done = set()
part2 = 0
for i in range(1 << len(nodes) - 1):
    print(i)
    if i in done:
        continue
    left = []
    right = []
    for j in range(len(nodes) - 1):
        if (1 << j) & i:
            left.append(nodes[1 + j])
        else:
            right.append(nodes[1 + j])
    start = mapping["AA"]
    left_pressure = dfs(start, 26, left, set())
    right_pressure = dfs(start, 26, right, set())
    done.add(i)
    done.add(~i)
    part2 = max(part2, left_pressure + right_pressure)

print(part2)
