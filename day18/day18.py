import sys
from collections import deque

filename = "./input.txt" if len(sys.argv) < 2 else sys.argv[1]
lines = [line.strip() for line in open(filename, "r").readlines()]

cubes = set()

for line in lines:
    x, y, z = [int(n) for n in line.split(",")]
    cubes.add((x, y, z))


def get_neighbors(node):
    x, y, z = node
    neighbors = []
    for dx, dy, dz in [
        (1, 0, 0),
        (-1, 0, 0),
        (0, 1, 0),
        (0, -1, 0),
        (0, 0, 1),
        (0, 0, -1),
    ]:
        neighbors.append((x + dx, y + dy, z + dz))
    return neighbors


trapped = set()
outside = set()


def check_if_trapped(node):
    global trapped, outside
    Q = deque([node])
    visited = set()
    limit = 2000

    while len(Q) > 0 and len(visited) < limit:
        node = Q.popleft()
        for neighbor in get_neighbors(node):
            if neighbor not in cubes and neighbor not in visited:
                Q.append(neighbor)
                visited.add(neighbor)
    if len(visited) < limit:
        trapped |= visited
    else:
        outside |= visited
    return len(visited) < limit


part1 = 0
part2 = 0

for cube in cubes:
    x, y, z = cube
    for neighbor in get_neighbors(cube):
        if neighbor in cubes:
            continue
        part1 += 1
        is_trapped = not neighbor in outside and (
            neighbor in trapped or check_if_trapped(neighbor)
        )
        if not is_trapped:
            part2 += 1

print(part1)
print(part2)
