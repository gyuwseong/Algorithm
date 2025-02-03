import sys
import collections

n, k = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))
counts = collections.defaultdict(int)

result = 0
start = 0

for end in range(n):
    counts[nums[end]] += 1
    while counts[nums[end]] > k:
        counts[nums[start]] -= 1
        start += 1
    result = max(result, end - start + 1)

print(result)
