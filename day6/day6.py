stream = open("./input.txt", "r").read()


def find_marker(stream, length):
    ans = 0
    for i in range(len(stream) - length):
        if len(set(stream[i : i + length])) == length:
            ans += i + length
            break
    return ans


print(find_marker(stream, 4))
print(find_marker(stream, 14))
