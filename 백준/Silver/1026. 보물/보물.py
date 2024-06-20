import collections
import sys

n = int(sys.stdin.readline())
a_lst = list(map(int, sys.stdin.readline().split()))
b_lst = list(map(int, sys.stdin.readline().split()))
q = collections.deque(sorted(b_lst, reverse=True))
s = 0
for a in sorted(a_lst):
    s += a * q.popleft()
print(s)