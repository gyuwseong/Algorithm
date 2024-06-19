import collections
import sys

t = int(sys.stdin.readline())
for _ in range(t):
    n, m = map(int, sys.stdin.readline().split())
    lst = list(map(int, sys.stdin.readline().split()))

    if n == 1:
        print(1)
        continue

    q = collections.deque(lst)
    start = 0
    while True:
        if q[0] != max(q):
            q.rotate(-1)
        else:
            v = q.popleft()
            start += 1
            if m == 0:
                print(start)
                break

        m = m - 1 if m > 0 else len(q) - 1
