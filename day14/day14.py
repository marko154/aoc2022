lines = [line.strip() for line in open("./input.txt", "r").readlines()]


def sign(n):
    if n >= 0:
        return 1
    return -1


rocks = set()
for line in lines:
    intervals = [
        [int(n) for n in interval.split(",")] for interval in line.split(" -> ")
    ]
    prev = intervals[0]
    for interval in intervals[1:]:
        px, py = prev
        tx, ty = interval

        for x in range(px, tx + sign(tx - px), sign(tx - px)):
            for y in range(py, ty + sign(ty - py), sign(ty - py)):
                rocks.add((x, y))
        prev = interval

sand = set()

lowest_rock = (0, 0)

for rock in rocks:
    if lowest_rock[1] < rock[1]:
        lowest_rock = rock

floor = lowest_rock[1] + 2
part1 = 0

while True:
    x, y = 500, 0
    if (x, y) in sand:
        break

    while True:
        if y > lowest_rock[1] and not part1:
            part1 = len(sand)
        bottom = (x, y + 1)
        left = (x - 1, y + 1)
        right = (x + 1, y + 1)

        bottom_occ = bottom in rocks or bottom in sand or y + 1 == floor
        left_occ = left in rocks or left in sand or y + 1 == floor
        right_occ = right in rocks or right in sand or y + 1 == floor

        if bottom_occ and left_occ and right_occ:
            sand.add((x, y))
            break

        if not bottom_occ:
            y += 1
        elif not left_occ:
            x -= 1
            y += 1
        elif not right_occ:
            x += 1
            y += 1
        else:
            sand.add((x, y))
            break

print(part1)
print(len(sand))
