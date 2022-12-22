import sys


filename = "./input.txt" if len(sys.argv) < 2 else sys.argv[1]
lines = [line.strip() for line in open(filename, "r").readlines()]

tree = {}

for line in lines:
    name, action = line.split(": ")
    tree[name] = action.split()


def evaluate(node):
    if len(tree[node]) == 1:
        return int(tree[node][0])
    left, op, right = tree[node]
    return eval(f"{evaluate(left)} {op} {evaluate(right)}")


print(int(evaluate("root")))


marked = {}


def traverse(node):
    if len(tree[node]) == 1:
        marked[node] = (int(tree[node][0]), node == "humn")
        return marked[node]

    left, op, right = tree[node]
    left, has_humn_l = traverse(left)
    right, has_humn_r = traverse(right)
    has_human = has_humn_r or has_humn_l
    value = eval(f"{left} {op} {right}")
    marked[node] = (value, has_human)
    return marked[node]


traverse("root")

node = "root"
left, op, right = tree[node]
l_val, has_humn_l = marked[left]
r_val, has_humn_r = marked[right]

node = left if has_humn_l else right
value = l_val if has_humn_r else r_val

while node != "humn":
    left, op, right = tree[node]
    l_val, has_humn_l = marked[left]
    r_val, _ = marked[right]

    if has_humn_l:
        if op == "+":
            value -= r_val
        elif op == "-":
            value += r_val
        elif op == "*":
            value /= r_val
        elif op == "/":
            value *= r_val
    else:
        if op == "+":
            value -= l_val
        elif op == "-":
            value = l_val - value
        elif op == "*":
            value /= l_val
        elif op == "/":
            value = l_val / value
    node = left if has_humn_l else right

print(int(value))
