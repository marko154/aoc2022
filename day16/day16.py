import re

lines = [line.strip() for line in open("./input.txt", "r").readlines()]

rates = [0] * len(lines)
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
    rates[mapping[v]] = rate

for via in range(len(matrix)):
    for fr in range(len(matrix)):
        for to in range(len(matrix)):
            matrix[fr][to] = min(matrix[fr][to], matrix[fr][via] + matrix[via][to])

start = mapping["AA"]
nodes = [i for i in range(len(matrix)) if rates[i] > 0]
# nodes.insert(0, start)


def dfs(valve, time, nodes, visited):
    global rates
    if time <= 0:
        return 0

    rate = rates[valve]
    visited.add(valve)
    max_pressure = 0

    for exit in nodes:
        dist = matrix[valve][exit]
        if exit not in visited:
            pressure = dfs(exit, time - dist - 1, nodes, visited)
            max_pressure = max(max_pressure, pressure)

    visited.discard(valve)
    return max_pressure + time * rate


part1 = dfs(start, 30, nodes, set())
print(part1)
part2 = 0


for i in range(1 << (len(nodes) - 1)):
    left = []
    right = []
    for j in range(len(nodes)):
        if (1 << j) & i:
            left.append(nodes[j])
        else:
            right.append(nodes[j])
    start = start
    left_pressure = dfs(start, 26, left, set())
    right_pressure = dfs(start, 26, right, set())
    part2 = max(part2, left_pressure + right_pressure)
print(part2)
