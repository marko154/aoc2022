lines = [line.strip() for line in open("./input.txt", "r").readlines()]

register = 1
cycle = 1
ans = 0

grid = [[":"] * 40 for x in range(6)]


def draw_pixel(grid, register, cycle):
    C = (cycle - 1) % 40
    if register - 1 <= C <= register + 1:
        grid[(cycle - 1) // 40][C] = "#"


for line in lines:
    line = line.split()
    if line[0] == "addx":
        draw_pixel(grid, register, cycle)
        if cycle % 40 == 20:
            ans += cycle * register
        cycle += 1

    draw_pixel(grid, register, cycle)

    if cycle % 40 == 20:
        ans += cycle * register

    if line[0] == "addx":
        register += int(line[1])
    cycle += 1


print(ans)

for line in grid:
    print("".join(line))
