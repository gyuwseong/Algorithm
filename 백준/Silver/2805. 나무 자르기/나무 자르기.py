import sys

n, m = map(int, sys.stdin.readline().split())
nums = sorted(list(map(int, sys.stdin.readline().split())))

start, end = 0, nums[-1]

while start <= end:
    mid = (start + end) // 2
    sums = sum((n - mid) for n in nums if n > mid)

    if sums >= m:
        start = mid + 1
    else:
        end = mid - 1
print(end)