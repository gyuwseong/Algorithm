import sys

n = int(sys.stdin.readline())
lst = [int(sys.stdin.readline()) for _ in range(n)]

min_n = lst[-1]
cnt = 0
for i in reversed(range(len(lst) - 1)):
    if lst[i] >= min_n:
        cnt += lst[i] - min_n + 1
        min_n -= 1
    else:
        min_n = lst[i]
print(cnt)