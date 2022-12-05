lines = [line.strip() for line in open("./input.txt", "r").readlines()]

input = """[D]                     [N] [F]    
[H] [F]             [L] [J] [H]    
[R] [H]             [F] [V] [G] [H]
[Z] [Q]         [Z] [W] [L] [J] [B]
[S] [W] [H]     [B] [H] [D] [C] [M]
[P] [R] [S] [G] [J] [J] [W] [Z] [V]
[W] [B] [V] [F] [G] [T] [T] [T] [P]
[Q] [V] [C] [H] [P] [Q] [Z] [D] [W]""".splitlines()

columns = [[] for i in range(9)]

for i in range(len(input) - 1, -1, -1):
    row = input[i]
    for j in range(1, len(row), 4):
        if row[j] != " ":
            columns[j // 4].append(row[j])

for line in lines:
    n, fr, to = [int(x) for x in line.split(" ") if x.isnumeric()]
    fr -= 1
    to -= 1
    # for i in range(min(n, len(M[fr]))):
    #     M[to].append(M[fr].pop())

    grabbed = columns[fr][-n:]
    columns[to].extend(grabbed)
    columns[fr] = columns[fr][:-n]

ans = "".join([col[-1] for col in columns])
print(ans)
