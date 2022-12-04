lines = [line.strip() for line in open("./input.txt", "r").readlines()]

ans = 0
ans2 = 0

for line in lines:
    a, b = line.split(",")
    s1, e1 = [int(n) for n in a.split("-")]
    s2, e2 = [int(n) for n in b.split("-")]

    start = max(s1, s2)
    end = min(e1, e2)

    if (start, end) in ((s1, e1), (s2, e2)):
        ans += 1

    if start <= end:
        ans2 += 1

print(ans)
print(ans2)
