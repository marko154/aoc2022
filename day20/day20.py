import sys

filename = "./input.txt" if len(sys.argv) < 2 else sys.argv[1]
lines = [line.strip() for line in open(filename, "r").readlines()]

arr = []
for line in lines:
    arr.append(int(line))


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


for i in range(len(arr)):
    arr[i] *= 811589153


head = Node(arr[0])
temp = head
mapping = {0: head}

for i, num in enumerate(arr[1:]):
    next = Node(num)
    temp.next = next
    temp = next
    mapping[i + 1] = next
temp.next = head


def get_predecessor(node):
    temp = node
    while temp.next != node:
        temp = temp.next
    return temp


def mix_list(arr, mapping):
    for i, num in enumerate(arr):
        node = mapping[i]
        assert node.value == num
        if num < 0:
            offset = len(arr) - 1 - abs(num)
            offset = offset % (len(arr) - 1)
        else:
            offset = num % (len(arr) - 1)

        temp = node
        predecessor = get_predecessor(node)
        for i in range(offset):
            predecessor.next = temp.next
            temp.next = temp.next.next
            predecessor.next.next = temp
            predecessor = predecessor.next


for i in range(10):
    mix_list(arr, mapping)

ans = 0
zero_idx = arr.index(0)
temp = mapping[zero_idx]

for i in range(3001):
    if i > 0 and i % 1000 == 0:
        ans += temp.value
        print(temp.value)
    temp = temp.next

print(ans)
