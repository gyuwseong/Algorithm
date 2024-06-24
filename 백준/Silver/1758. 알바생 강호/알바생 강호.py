import sys

n = int(sys.stdin.readline())
lst = sorted([int(sys.stdin.readline()) for i in range(n)], reverse=True)

cnt = 0
for i, l in enumerate(lst):
    t = l - (i - 1 + 1)
    if t > 0:
        cnt += t
print(cnt)