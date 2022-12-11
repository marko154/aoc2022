import re
from copy import deepcopy

data = open("./input.txt", "r").read()

monkeys = []
prime_prod = 1

for monkey_str in data.split("\n\n"):
    lines = monkey_str.splitlines()
    monkey = {
        "items": [int(n) for n in re.findall(r"\d+", lines[1])],
        "op": lines[2].replace("Operation: new = ", "").strip(),
        "test": int(lines[3].split()[-1]),
        "true": int(lines[4].split()[-1]),
        "false": int(lines[5].split()[-1]),
    }
    monkeys.append(monkey)
    prime_prod *= monkey["test"]


def simulate(monkeys, rounds, after_op):
    ins = [0] * len(monkeys)

    for i in range(rounds):
        for j in range(len(monkeys)):
            monkey = monkeys[j]
            for old in monkey["items"]:
                ins[j] += 1
                new = eval(monkey["op"])
                new = after_op(new)
                if new % monkey["test"] == 0:
                    monkeys[monkey["true"]]["items"].append(new)
                else:
                    monkeys[monkey["false"]]["items"].append(new)
            monkey["items"] = []

    ins.sort()
    return ins[-1] * ins[-2]


print(simulate(deepcopy(monkeys), 20, lambda new: (new // 3)))
print(simulate(monkeys, 10000, lambda new: new % prime_prod))
