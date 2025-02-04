import sys

n, m = map(int, sys.stdin.readline().split())
if m <= 0:
    print(0)
else:
    nums = sorted(list(int(sys.stdin.readline().strip()) for _ in range(n)))
    result = 2000000000
    start = 0

    for end in range(n):
        while nums[end] - nums[start] >= m:
            result = min(result, nums[end] - nums[start])
            start += 1
    print(result)
