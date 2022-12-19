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


def dfs(time, costs, robots, rocks):
    global TEMP
    if time <= 0:
        if rocks["geode"] > TEMP:
            TEMP = rocks["geode"]
            print(TEMP)
        return rocks["geode"]

    def create_rocks():
        new_rocks = rocks.copy()
        for rock in robots:
            new_rocks[rock] += robots[rock]
        return new_rocks
    possibles = []
    best = 0
    was_geode = False
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
    max_obsidian = costs["geode"][1]
    if rocks["ore"] >= costs["obsidian"][0] and rocks["clay"] >= costs["obsidian"][1] and robots["obsidian"] < max_obsidian:
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
        while
        new_rocks["ore"] -= costs["clay"][0]
        possible = dfs(time - 1, costs, new_robots, new_rocks)
        possibles.append(possible)
        best = max(possible, best)
    # ore
    max_ore = max(x[0] for x in costs.values())
    if rocks["ore"] >= costs["ore"][0] and robots["ore"] < 2:
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
    best = dfs(24, costs, robots, rocks)
    print(costs, robots, rocks)
    print(best)
    ans += (i + 1) * best


print(ans)
