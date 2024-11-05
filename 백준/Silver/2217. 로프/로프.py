import sys

n = int(sys.stdin.readline().strip())
lst = sorted(list(int(sys.stdin.readline().strip()) for _ in range(n)), reverse=True)
rst = 0
for i in range(n):
    if lst[i] * (i + 1) > rst:
        rst = lst[i] * (i + 1)
print(rst)