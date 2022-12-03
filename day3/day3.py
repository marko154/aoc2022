lines = [line.strip() for line in open("./input.txt", "r").readlines()]


def get_score(ch):
    if ch.lower() == ch:
        return ord(ch) - ord("a") + 1
    else:
        return ord(ch) - ord("A") + 27


same = []

for line in lines:
    l = set(line[: len(line) // 2])
    r = set(line[len(line) // 2 :])
    same.append((l & r).pop())

ans = sum(get_score(ch) for ch in same)

badges = []

for i in range(0, len(lines), 3):
    common = set(lines[i])
    common &= set(lines[i + 1])
    common &= set(lines[i + 2])

    badges.append(common.pop())

ans2 = sum(get_score(badge) for badge in badges)

print(ans)
print(ans2)
