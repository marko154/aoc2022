lines = [line.strip() for line in open("./input.txt", "r").readlines()]

elves = []
elf = 0

for line in lines:
    if line:
        elf += int(line)
    else:
        elves.append(elf)
        elf = 0

elves.sort(reverse=True)
print(elves[0])
print(sum(elves[:3]))
