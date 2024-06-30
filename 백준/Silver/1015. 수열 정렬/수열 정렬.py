import sys

n = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))

cnt = 0
rst = [0] * n
s_lst = sorted(lst)
for s in s_lst:
    idx = lst.index(s)
    rst[idx] = cnt
    cnt += 1
    lst[idx] = 0

print(*rst)
