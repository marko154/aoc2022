lines = [line.strip() for line in open("./input.txt", "r").readlines()]

scores = {
    "A": 1,
    "B": 2,
    "C": 3,
}

win = {
    "A": "C",
    "B": "A",
    "C": "B",
}

lose = {v: k for k, v in win.items()}

M = {
    "X": "A",
    "Y": "B",
    "Z": "C",
}

ans = 0


for line in lines:
    a, b = [n for n in line.split()]
    b = M[b]
    s1 = scores[a]
    s2 = scores[b]

    if win[b] == a:
        ans += s2 + 6
    elif b == a:
        ans += s2 + 3
    else:
        ans += s2

print(ans)
ans = 0

for line in lines:
    a, outcome = [n for n in line.split()]

    s1 = scores[a]

    if outcome == "X":
        ans += scores[win[a]]
    elif outcome == "Z":
        ans += 6 + scores[lose[a]]
    else:
        ans += 3 + scores[a]

print(ans)
