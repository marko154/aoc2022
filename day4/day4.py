lines = [line.strip() for line in open("./input.txt", "r").readlines()]

ans = 0
ans2 = 0

for line in lines:
    a, b = line.split(",")

    r1 = [int(n) for n in a.split("-")]
    r2 = [int(n) for n in b.split("-")]

    s1 = set(range(r1[0], r1[1] + 1))
    s2 = set(range(r2[0], r2[1] + 1))

    if len(s1 & s2) == min(len(s1), len(s2)):
        ans += 1

    if len(s1 & s2) > 0:
        ans2 += 1

print(ans)
print(ans2)
