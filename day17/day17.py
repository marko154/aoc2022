shapes = [
    ["####"],
    [
        ".#.",
        "###",
        ".#.",
    ],
    [
        "..#",
        "..#",
        "###",
    ],
    [
        "#",
        "#",
        "#",
        "#",
    ],
    ["##", "##"],
]

stream = open("./input.txt", "r").read()
GH = 10000


def collides(grid, si, sj, shape):
    global shapes
    if si >= len(grid):
        return True
    for i in range(len(shape)):
        for j in range(len(shape[0])):
            if shape[i][j] == "#" and grid[si - len(shape) + 1 + i][sj + j] == "#":
                return True
    return False


def place_in_grid(grid, si, sj, shape):
    for i in range(len(shape)):
        for j in range(len(shape[0])):
            if shape[i][j] == "#":
                grid[si - len(shape) + 1 + i][sj + j] = "#"


def get_height(iterations):
    global stream, GH
    read_ptr = 0

    fallen = 0
    sidx = 0

    grid = [["."] * 7 for x in range(GH)]
    si = len(grid) - 4
    sj = 2

    top = GH - 1

    while fallen < iterations:
        shape = shapes[sidx]
        dir = stream[read_ptr]
        read_ptr = (read_ptr + 1) % len(stream)
        if dir == "<" and sj > 0:
            if not collides(grid, si, sj - 1, shape):
                sj -= 1
        if dir == ">" and sj + 1 + len(shape[0]) <= 7:
            if not collides(grid, si, sj + 1, shape):
                sj += 1

        if collides(grid, si + 1, sj, shape):
            place_in_grid(grid, si, sj, shape)
            sidx = (sidx + 1) % len(shapes)
            top = min(top, si - len(shape))
            sj = 2
            si = top - 3
            fallen += 1
        else:
            si += 1
    return GH - 1 - top


# part 1
print(get_height(2022))

recurrence = [
    33,
    89,
    31,
    235,
    87,
    121,
    35,
    142,
    16,
    340,
    14,
    139,
    10,
    106,
    27,
    51,
    38,
    11,
    220,
]

# part 2
start = 2022
total = 1000000000000
recurence_size = sum(recurrence)
reccurence_height = get_height(start + recurence_size) - get_height(start)

print(
    ((total - start) // recurence_size) * reccurence_height
    + get_height(start + (total - start) % recurence_size)
)
