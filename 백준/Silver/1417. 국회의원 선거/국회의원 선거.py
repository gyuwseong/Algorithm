import heapq
import sys

n = int(sys.stdin.readline())
ipt_lst = [int(sys.stdin.readline().strip()) for _ in range(n)]

target = ipt_lst[0]
cnt = 0
lst = [-i for i in ipt_lst[1:]]
heapq.heapify(lst)

while lst:
    max_value = -heapq.heappop(lst)
    if max_value < target:
        break
    target += 1
    cnt += 1
    heapq.heappush(lst, -(max_value - 1))

print(cnt)