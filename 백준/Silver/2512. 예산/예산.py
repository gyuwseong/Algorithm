import sys

n = int(sys.stdin.readline().strip())
nums = sorted(list(map(int, sys.stdin.readline().split())))
target = int(sys.stdin.readline().strip())

start, end = 0, nums[-1]
while start <= end:
    mid = (start + end) // 2
    result = sum(min(num, mid) for num in nums)

    if result <= target:
        start = mid + 1
    else:
        end = mid - 1

print(end)