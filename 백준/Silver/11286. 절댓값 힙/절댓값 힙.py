import sys
import heapq

n = int(sys.stdin.readline().strip())
ph = []
nh = []

for _ in range(n):
    x = int(sys.stdin.readline().strip())
    if x == 0:
        if ph and not nh:
            print(heapq.heappop(ph))
        elif nh and not ph:
            print(-heapq.heappop(nh))
        elif ph and nh:
            if ph[0] >= abs(nh[0]):
                print(-heapq.heappop(nh))
            else:
                print(heapq.heappop(ph))
        else:
            print(0)
    else:
        if x > 0:
            heapq.heappush(ph, x)
        else:
            heapq.heappush(nh, -x)
