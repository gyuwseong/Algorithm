import sys

n = int(sys.stdin.readline())
lst = sorted([int(sys.stdin.readline()) for i in range(n)], reverse=True)

for i in range(n):
    if lst[i] < sum(lst[i + 1:i + 3]):
        print(sum(lst[i:i + 3]))
        break
else:
    print(-1)