lines = [line.strip() for line in open("./input.txt", "r").readlines()]

dirs = {
    "R": (0, 1),
    "L": (0, -1),
    "U": (1, 0),
    "D": (-1, 0),
}


def should_move(knot1, knot2):
    for i in range(-1, 2):
        for j in range(-1, 2):
            if knot1[0] + i == knot2[0] and knot1[1] + j == knot2[1]:
                return False
    return True


def get_num_of_tail_visited(directions, snake_length):
    knots = [[0, 0] for i in range(snake_length)]

    visited = set()

    for line in lines:
        dir, steps = line.split()
        steps = int(steps)

        dy, dx = dirs[dir]
        for _ in range(steps):
            head = knots[0]
            head[0] += dx
            head[1] += dy

            i = 1

            while i < len(knots) and should_move(head, knots[i]):
                knot = knots[i]
                tdx = head[0] - knot[0]
                tdy = head[1] - knot[1]
                if tdx != 0:
                    tdx = tdx // abs(tdx)
                if tdy != 0:
                    tdy = tdy // abs(tdy)

                knot[0] += tdx
                knot[1] += tdy
                head = knot
                i += 1
            visited.add(tuple(knots[-1]))
    return len(visited)


print(get_num_of_tail_visited(lines, 2))
print(get_num_of_tail_visited(lines, 10))
