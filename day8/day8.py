lines = [line.strip() for line in open("./input.txt", "r").readlines()]


ans = len(lines) * 4 - 4
ans2 = 0
tp = list(zip(*lines))

for i in range(1, len(lines) - 1):
    for j in range(1, len(lines) - 1):
        curr = int(lines[i][j])
        l = [int(x) for x in lines[i][:j]][::-1]
        r = [int(x) for x in lines[i][j + 1 :]]
        t = [int(x) for x in tp[j][:i]][::-1]
        b = [int(x) for x in tp[j][i + 1 :]]
        dirs = [l, r, t, b]

        if any(max(line) < curr for line in dirs):
            ans += 1

        score = 1

        for line in dirs:
            line_score = 0
            for tree in line:
                line_score += 1
                if int(tree) >= curr:
                    break
            score *= line_score
        ans2 = max(ans2, score)

print(ans)
print(ans2)
