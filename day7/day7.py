lines = [line.strip() for line in open("./input.txt", "r").readlines()]


def new_node(parent):
    return {"parent": parent, "filesizes": [], "dirs": {}}


fs = new_node(None)
current = fs
ptr = 0


while ptr < len(lines):
    line = lines[ptr].split()
    command = line[1]
    arg = "" if len(line) < 3 else line[2]
    ptr += 1
    if command == "cd":
        if arg == "/":
            current = fs
        if arg == "..":
            if current["parent"]:
                current = current["parent"]
        else:
            if arg not in current["dirs"]:
                current["dirs"][arg] = new_node(current)
            current = current["dirs"][arg]
    elif command == "ls":
        while ptr < len(lines) and not lines[ptr].startswith("$"):
            size, _ = lines[ptr].split()
            if size != "dir":
                current["filesizes"].append(int(size))
            ptr += 1

sizes = []


def get_size(node):
    global sizes
    size = sum(x for x in node["filesizes"])
    for nnode in node["dirs"].values():
        size += get_size(nnode)
    sizes.append(size)
    return size


used = get_size(fs)
excess = 30000000 - (70000000 - used)

ans = sum(s for s in sizes if s <= 100000)
ans2 = sorted([s for s in sizes if s >= excess])[0]

print(ans)
print(ans2)
