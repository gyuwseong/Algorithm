import sys

n, m = map(int, sys.stdin.readline().split())
lst = sorted([int(sys.stdin.readline().strip()) for _ in range(m)])

rst, idx = 0, 0
for i, value in enumerate(lst):
    cnt = value * min(m - i, n)
    if cnt > rst:
        rst, idx = cnt, value
print(idx, rst)