import sys
import collections

n = int(sys.stdin.readline().strip())
a_lst = list(map(int, sys.stdin.readline().split()))
b_lst = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline().strip())
c_lst = list(map(int, sys.stdin.readline().split()))
q = collections.deque()

for idx, b in enumerate(b_lst):
    if a_lst[idx] == 0:
        q.append(b)

result = []
for c in c_lst:
    q.appendleft(c)
    result.append(q.pop())

print(*result)
