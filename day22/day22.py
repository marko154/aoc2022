import re  # search, findall, replace
import sys

filename = "./input.txt" if len(sys.argv) < 2 else sys.argv[1]
grid, dirs_str = open(filename, "r").read().split("\n\n")
grid = grid.splitlines()
max_w = max(len(row) for row in grid)

for i, row in enumerate(grid):
    grid[i] = row + (max_w - len(row)) * " "

points = {}
pos = None

for i, row in enumerate(grid):
    for j, cell in enumerate(row):
        if cell in (".", "#"):
            if not pos:
                pos = (i, j)
            outgoing = []

            # top
            ti = (i - 1) % len(grid)
            while grid[ti][j] == " ":
                ti = (ti - 1) % len(grid)
            outgoing.append([(ti, j), 0])
            # right
            rj = (j + 1) % len(row)
            while grid[i][rj] == " ":
                rj = (rj + 1) % len(row)
            outgoing.append([(i, rj), 0])
            # bottom
            bi = (i + 1) % len(grid)
            while grid[bi][j] == " ":
                bi = (bi + 1) % len(grid)
            outgoing.append([(bi, j), 0])
            # left
            lj = (j - 1) % len(row)
            while grid[i][lj] == " ":
                lj = (lj - 1) % len(row)
            outgoing.append([(i, lj), 0])
            points[(i, j)] = [grid[i][j], outgoing]

dirs = [(dir[-1], int(dir[:-1])) for dir in re.findall(r"\d+[RL]", dirs_str)]
dirs.append((None, int(re.findall(r"\d+", dirs_str)[0])))


def compute_cube_edges():
    global points
    top, right, bottom, left = range(4)
    # 1
    for k in range(50):
        points[(0, 50 + k)][1][top][0] = (150 + k, 0)
        points[(0, 50 + k)][1][top][1] = 1

        points[(150 + k, 0)][1][left][0] = (0, 50 + k)
        points[(150 + k, 0)][1][left][1] = 3

    # 2
    for k in range(50):
        points[(0, 100 + k)][1][top][0] = (199, k)
        points[(199, k)][1][bottom][0] = (0, 100 + k)

    # 3
    for k in range(50):
        points[(k, 149)][1][right][0] = (149 - k, 99)
        points[(k, 149)][1][right][1] = 2

        points[(149 - k, 99)][1][right][0] = (k, 149)
        points[(149 - k, 99)][1][right][1] = 2

    # 4
    for k in range(50):
        points[(k, 50)][1][left][0] = (149 - k, 0)
        points[(k, 50)][1][left][1] = 2

        points[(149 - k, 0)][1][left][0] = (k, 50)
        points[(149 - k, 0)][1][left][1] = 2

    # 5
    for k in range(50):
        points[(50 + k, 50)][1][left][0] = (100, k)
        points[(50 + k, 50)][1][left][1] = 3

        points[(100, k)][1][top][0] = (50 + k, 50)
        points[(100, k)][1][top][1] = 1

    # 6
    for k in range(50):
        points[(149, k + 50)][1][bottom][0] = (150 + k, 49)
        points[(149, k + 50)][1][bottom][1] = 1

        points[(150 + k, 49)][1][right][0] = (149, k + 50)
        points[(150 + k, 49)][1][right][1] = 3

    # 7
    for k in range(50):
        points[(49, k + 100)][1][bottom][0] = (50 + k, 99)
        points[(49, k + 100)][1][bottom][1] = 1

        points[(50 + k, 99)][1][right][0] = (49, k + 100)
        points[(50 + k, 99)][1][right][1] = 3


def solve(dirs, pos):
    curr_dir = 1
    for dir, steps in dirs:
        for _ in range(steps):
            _, outgoing = points[pos]
            maybe_next, offset = outgoing[curr_dir]
            if points[maybe_next][0] == ".":
                curr_dir = (curr_dir + offset) % 4
                pos = maybe_next
        if dir == "R":
            curr_dir = (curr_dir + 1) % 4
        elif dir == "L":
            curr_dir = (curr_dir + 3) % 4

    facing = (curr_dir + 3) % 4
    i, j = pos
    return 1000 * (i + 1) + 4 * (j + 1) + facing


print(solve(dirs, pos))
compute_cube_edges()
print(solve(dirs, pos))
