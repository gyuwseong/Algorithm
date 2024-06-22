import sys

n = int(sys.stdin.readline())
lst = [list(map(int, sys.stdin.readline().split())) for i in range(n)]
sorted_lst = sorted(lst, key=lambda x: (x[1], x[0]))

cnt = 0
start = sorted_lst[0][0]
for s in sorted_lst:
    if s[0] < start:
        pass
    elif s[0] >= start:
        cnt += 1
        start = s[1]
print(cnt)