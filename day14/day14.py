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

lowest_rock = 0

for rock in rocks:
    if lowest_rock < rock[1]:
        lowest_rock = rock[1]

floor = lowest_rock + 2
part1 = 0
part2 = 0

while True:
    x, y = 500, 0
    if (x, y) in rocks:
        break

    while True:
        if y > lowest_rock and not part1:
            part1 = part2
        bottom = (x, y + 1)
        left = (x - 1, y + 1)
        right = (x + 1, y + 1)

        if y + 1 >= floor:
            rocks.add((x, y))
            part2 += 1
            break

        if not bottom in rocks:
            y += 1
        elif not left in rocks:
            x -= 1
            y += 1
        elif not right in rocks:
            x += 1
            y += 1
        else:
            rocks.add((x, y))
            part2 += 1
            break

print(part1)
print(part2)
