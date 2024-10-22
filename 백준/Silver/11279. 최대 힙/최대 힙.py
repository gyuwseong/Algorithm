import sys
import heapq

n = int(sys.stdin.readline().strip())
h = []

for _ in range(n):
    x = int(sys.stdin.readline().strip())
    if x > 0:
        heapq.heappush(h, -x)
    else:
        if h:
            print(-heapq.heappop(h))
        else:
            print(0)