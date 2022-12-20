import re  # search, findall, replace
from collections import defaultdict, deque, Counter, OrderedDict
import heapq
import bisect
from itertools import combinations, combinations_with_replacement, permutations, product
import sys
from time import sleep

filename = "./input.txt" if len(sys.argv) < 2 else sys.argv[1]
lines = [line.strip() for line in open(filename, "r").readlines()]


# ore, clay, obsidian, geode
TEMP = 0


def pick_robot(costs, robots, rocks):
    # if can build a geode robot return geode
    if rocks["ore"] >= costs["geode"][0] and rocks["obsidian"] >= costs["geode"][1]:
        return "geode"
    # else
    #

    pass


# Each ore robot costs 4 ore.
# Each clay robot costs 2 ore.
# Each obsidian robot costs 3 ore and 14 clay.
# Each geode robot costs 2 ore and 7 obsidian.


def dfs(time, costs, robots, rocks):
    global TEMP
    if time <= 0:
        if rocks["geode"] > TEMP:
            TEMP = rocks["geode"]
            print(TEMP)
        return rocks["geode"]

    possibles = []
    best = 0
    was_geode = False
    time_left = time
    max_geodes = time_left * (time_left + 1) // 2

    sleep(1)

    print(time, robots, rocks)

    # geode
    if rocks["ore"] >= costs["geode"][0] and rocks["obsidian"] >= costs["geode"][1]:
        new_robots = robots.copy()
        new_robots["geode"] += 1
        new_rocks = create_rocks()
        new_rocks["ore"] -= costs["geode"][0]
        new_rocks["obsidian"] -= costs["geode"][1]
        possible = dfs(time - 1, costs, new_robots, new_rocks)
        possibles.append(possible)
        best = max(possible, best)
        was_geode = True
    # obsidian
    if best >= max_geodes:
        # print(max_geodes)
        return best

    max_obsidian = costs["geode"][1]
    if (
        rocks["ore"] >= costs["obsidian"][0]
        and rocks["clay"] >= costs["obsidian"][1]
        and robots["obsidian"] < max_obsidian
    ):
        new_robots = robots.copy()
        new_robots["obsidian"] += 1
        new_rocks = create_rocks()
        new_rocks["ore"] -= costs["obsidian"][0]
        new_rocks["clay"] -= costs["obsidian"][1]
        possible = dfs(time - 1, costs, new_robots, new_rocks)
        possibles.append(possible)
        best = max(possible, best)
    # clay
    max_clay = costs["obsidian"][1]
    if rocks["ore"] >= costs["clay"][0] and robots["clay"] < max_clay:
        new_robots = robots.copy()
        new_robots["clay"] += 1
        new_rocks = create_rocks()
        new_rocks["ore"] -= costs["clay"][0]
        possible = dfs(time - 1, costs, new_robots, new_rocks)
        possibles.append(possible)
        best = max(possible, best)

    # ore
    max_ore = max(x[0] for x in costs.values())
    if rocks["ore"] >= costs["ore"][0] and robots["ore"] < max_ore:
        new_robots = robots.copy()
        new_robots["ore"] += 1
        new_rocks = create_rocks()
        new_rocks["ore"] -= costs["ore"][0]
        possible = dfs(time - 1, costs, new_robots, new_rocks)
        possibles.append(possible)
        best = max(possible, best)

    # if no robots were created
    if not was_geode:
        possible = dfs(time - 1, costs, robots, create_rocks())
        possibles.append(possible)
        best = max(possible, best)

    return best


ans = 0
names = ["ore", "clay", "obsidian", "geode"]


for i, line in enumerate(lines):
    robots = line.split(": ")[1].split(". ")
    costs = {}
    for j, robot in enumerate(robots):
        costs[names[j]] = tuple(map(int, re.findall(r"\d+", robot)))
    robots = {"ore": 1, "clay": 0, "obsidian": 0, "geode": 0}
    rocks = {"ore": 0, "clay": 0, "obsidian": 0, "geode": 0}
    # best = dfs(24, costs, robots, rocks)
    best = 0

    Q = deque()
    Q.append((1, robots, rocks))

    max_obsidian = costs["geode"][1]
    max_clay = costs["obsidian"][1]
    max_ore = max(x[0] for x in costs.values())
    best_so_far = None
    ans = 0
    while Q:
        time, robots, rocks = Q.popleft()
        ans = max(ans, rocks["geode"])
        if robots["geode"] > 0:
            if not best_so_far or best_so_far[1]["geode"] < robots["geode"]:
                best_so_far = (time, robots, rocks)
            print(time, len(Q), rocks, robots)
        if best_so_far and best_so_far[1]["geode"] < robots["geode"]:
            continue
        if time == 24 or len(Q) > 7_000_000:
            print(len(Q))
            break
        was_geode = False
        next_rocks = rocks.copy()
        for rock in robots:
            next_rocks[rock] += robots[rock]

        if rocks["ore"] >= costs["geode"][0] and rocks["obsidian"] >= costs["geode"][1]:
            new_robots = robots.copy()
            new_robots["geode"] += 1
            new_rocks = next_rocks.copy()
            new_rocks["ore"] -= costs["geode"][0]
            new_rocks["obsidian"] -= costs["geode"][1]
            Q.append((time + 1, new_robots, new_rocks))
            was_geode = True
        # obsidian
        if (
            rocks["ore"] >= costs["obsidian"][0]
            and rocks["clay"] >= costs["obsidian"][1]
            and robots["obsidian"] < max_obsidian
        ):
            new_robots = robots.copy()
            new_robots["obsidian"] += 1
            new_rocks = next_rocks.copy()
            new_rocks["ore"] -= costs["obsidian"][0]
            new_rocks["clay"] -= costs["obsidian"][1]
            if not was_geode:
                Q.append((time + 1, new_robots, new_rocks))
        # clay
        if rocks["ore"] >= costs["clay"][0] and robots["clay"] < max_clay:
            new_robots = robots.copy()
            new_robots["clay"] += 1
            new_rocks = next_rocks.copy()
            new_rocks["ore"] -= costs["clay"][0]
            if not was_geode:
                Q.append((time + 1, new_robots, new_rocks))

        # ore
        if rocks["ore"] >= costs["ore"][0] and robots["ore"] < max_ore:
            new_robots = robots.copy()
            new_robots["ore"] += 1
            new_rocks = next_rocks.copy()
            new_rocks["ore"] -= costs["ore"][0]
            if not was_geode:
                Q.append((time + 1, new_robots, new_rocks))

        # if no robots were created
        if not was_geode:
            Q.append((time + 1, robots, next_rocks))

    print(costs, robots, rocks)
    print(ans, "!" * 20)
    break
    ans += (i + 1) * best


print(ans)
