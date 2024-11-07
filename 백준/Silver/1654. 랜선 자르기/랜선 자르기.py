import sys

k, n = map(int, sys.stdin.readline().split())
lst = list(int(sys.stdin.readline().strip()) for _ in range(k))
start, end = 1, max(lst)

while start <= end:
    mid = (start + end) // 2
    count = min(n, sum([l // mid for l in lst]))
    if count >= n:
        start = mid + 1
    else:
        end = mid - 1

print(end)