import re  # search, findall, replace
import sys

filename = "./input.txt" if len(sys.argv) < 2 else sys.argv[1]
lines = [line.strip() for line in open(filename, "r").readlines()]

part1 = 0
names = ["ore", "clay", "obsidian", "geode"]


def solve(end, oreC, clayC, obsC, geodeC):
    init_robots = (1, 0, 0, 0)
    init_rocks = (0, 0, 0, 0)
    seen = set()
    stack = []
    stack.append((0, init_robots, init_rocks))

    max_obsidian = geodeC[1]
    max_clay = obsC[1]
    max_ore = max(oreC, clayC, obsC[0], geodeC[0])

    best = 0

    while stack:
        state = stack.pop()
        time, robots, rocks = state
        ore, clay, obs, geode = rocks
        oreR, clayR, obsR, geodeR = robots
        best = max(best, geode)

        if time >= end:
            continue

        oreR = min(max_ore, oreR)
        clayR = min(max_clay, clayR)
        obsR = min(max_obsidian, obsR)

        # remove rocks if you can never spend them to get better memoization
        ore = min((end - time) * max_ore - (end - 1 - time) * oreR, ore)
        clay = min((end - time) * max_clay - (end - 1 - time) * clayR, clay)
        obs = min((end - time) * max_obsidian - (end - 1 - time) * obsR, obs)

        key = (time, (oreR, clayR, obsR, geodeR), (ore, clay, obs, geode))
        if key in seen:
            continue

        seen.add(key)

        n_ore = ore + oreR
        n_clay = clay + clayR
        n_obs = obs + obsR
        n_geode = geode + geodeR
        qsize = len(stack)

        # geode
        if ore >= geodeC[0] and obs >= geodeC[1]:
            stack.append(
                (
                    time + 1,
                    (oreR, clayR, obsR, geodeR + 1),
                    (n_ore - geodeC[0], n_clay, n_obs - geodeC[1], n_geode),
                )
            )
            continue
        # obsidian
        if ore >= obsC[0] and clay >= obsC[1]:
            stack.append(
                (
                    time + 1,
                    (oreR, clayR, obsR + 1, geodeR),
                    (n_ore - obsC[0], n_clay - obsC[1], n_obs, n_geode),
                )
            )
            continue
        # clay
        if ore >= clayC:
            stack.append(
                (
                    time + 1,
                    (oreR, clayR + 1, obsR, geodeR),
                    (n_ore - clayC, n_clay, n_obs, n_geode),
                )
            )

        # ore
        if ore >= oreC:
            stack.append(
                (
                    time + 1,
                    (oreR + 1, clayR, obsR, geodeR),
                    (n_ore - oreC, n_clay, n_obs, n_geode),
                )
            )

        if qsize + 4 != len(stack):
            stack.append(
                (
                    time + 1,
                    (oreR, clayR, obsR, geodeR),
                    (n_ore, n_clay, n_obs, n_geode),
                )
            )
    return best


part1 = 0
part2 = 1

for i, line in enumerate(lines):
    data = line.split(": ")[1].split(". ")
    parsed_costs = [tuple(map(int, re.findall(r"\d+", robot)))
                    for robot in data]

    oreC = parsed_costs[0][0]
    clayC = parsed_costs[1][0]
    obsC = (parsed_costs[2][0], parsed_costs[2][1])
    geodeC = (parsed_costs[3][0], parsed_costs[3][1])
    if i < 3:
        part2 *= solve(32, oreC, clayC, obsC, geodeC)

    best = solve(24, oreC, clayC, obsC, geodeC)
    part1 += (i + 1) * best


print(part1)
print(part2)
