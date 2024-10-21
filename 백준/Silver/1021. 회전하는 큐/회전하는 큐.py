import sys
import collections

n, k = map(int, sys.stdin.readline().split())
lst = list(int(i) for i in range(1, n + 1))
loca_lst = list(map(int, sys.stdin.readline().split()))
q = collections.deque(lst)

cnt = 0
for i in loca_lst:
    while q[0] != i:
        i_idx = q.index(i)
        if i_idx <= len(q) // 2:
            q.rotate(-1)
            cnt += 1
        else:
            q.rotate()
            cnt += 1
    q.popleft()
print(cnt)