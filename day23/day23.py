from collections import defaultdict
import sys

filename = "./input.txt" if len(sys.argv) < 2 else sys.argv[1]
lines = [line.strip() for line in open(filename, "r").readlines()]

elves = set()

for y, row in enumerate(lines):
    for x, cell in enumerate(row):
        if cell == "#":
            elves.add((x, -y))

views = [
    ((-1, 1), (0, 1), (1, 1)),  # N
    ((-1, -1), (0, -1), (1, -1)),  # S
    ((-1, 1), (-1, 0), (-1, -1)),  # W
    ((1, 1), (1, 0), (1, -1)),  # E
]


def count_empty_tiles():
    tiles = 0
    left = min(x for x, y in elves)
    right = max(x for x, y in elves)
    top = max(y for x, y in elves)
    bottom = min(y for x, y in elves)
    for y in range(top, bottom - 1, -1):
        for x in range(left, right + 1):
            if (x, y) not in elves:
                tiles += 1
    return tiles


round = 0

while True:
    proposal_counter = defaultdict(int)
    proposals = {}
    for elf in elves:
        wants_to_move = False
        ex, ey = elf

        for dx in range(-1, 2):
            for dy in range(-1, 2):
                if dy == dx == 0:
                    continue
                if (ex + dx, ey + dy) in elves:
                    wants_to_move = True
        if not wants_to_move:
            continue

        for i in range(4):
            can_move = True
            for dx, dy in views[(round + i) % 4]:
                if (ex + dx, ey + dy) in elves:
                    can_move = False
                    break
            if can_move:
                dx, dy = views[(round + i) % 4][1]
                proposal = (ex + dx, ey + dy)
                proposals[elf] = proposal
                proposal_counter[proposal] += 1
                break

    next_elves = set()
    moved = False
    for elf in elves:
        if elf not in proposals or proposal_counter[proposals[elf]] > 1:
            next_elves.add(elf)
        else:
            moved = True
            next_elves.add(proposals[elf])
    elves = next_elves

    round += 1
    if round == 10:
        print(count_empty_tiles())
    if not moved:
        break

print(round)
