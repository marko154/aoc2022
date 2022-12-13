import numpy as np


pairs = open("./input.txt", "r").read().split("\n\n")
ans = 0


def cmp(item1, item2):
    if type(item1) == type(item2) == int:
        if item1 < item2:
            return 1
        elif item1 == item2:
            return 0
        return -1
    elif list == type(item1) and type(item2) == int:
        item2 = [item2]
    elif list == type(item2) and type(item1) == int:
        item1 = [item1]

    for i in range(min(len(item1), len(item2))):
        el1 = item1[i]
        el2 = item2[i]
        if cmp(el1, el2) == 1:
            return 1
        if cmp(el1, el2) == -1:
            return -1
    if len(item1) < len(item2):
        return 1
    elif len(item1) == len(item2):
        return 0
    return -1


arrays = []

for i, pair in enumerate(pairs):
    pair = pair.splitlines()
    arr1 = eval(pair[0])
    arr2 = eval(pair[1])
    arrays.append(arr1)
    arrays.append(arr2)
    if cmp(arr1, arr2) == 1:
        ans += i + 1

arrays.append([[2]])
arrays.append([[6]])


for i in range(len(arrays) - 1):
    for j in range(0, len(arrays) - 1 - i):
        if cmp(arrays[j], arrays[j + 1]) == -1:
            arrays[j], arrays[j + 1] = arrays[j + 1], arrays[j]


ans2 = 1
for i in range(len(arrays)):
    if arrays[i] in ([[2]], [[6]]):
        ans2 *= i + 1

print(ans)
print(ans2)
