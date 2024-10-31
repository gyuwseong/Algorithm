import sys

ipt = sys.stdin.readline().strip()
stack = []
result = []
i, j = 0, 0

while i < len(ipt):
    if ipt[i] == "<":
        while stack:
            result.append(stack.pop())

        for j in range(i + 1, len(ipt)):
            if ipt[j] == ">":
                result.append(ipt[i:j + 1])
                break
        i = j + 1
    else:
        if ipt[i] == " ":
            while stack:
                result.append(stack.pop())
            result.append(ipt[i])
        else:
            stack.append(ipt[i])
        i += 1

while stack:
    result.append(stack.pop())

for r in result:
    print(r, end="")
