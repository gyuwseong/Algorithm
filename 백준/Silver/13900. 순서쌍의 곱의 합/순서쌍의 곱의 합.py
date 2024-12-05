import sys

n = int(sys.stdin.readline().strip())
nums = list(map(int, sys.stdin.readline().split()))
result = 0
sums = sum(nums)
for i in range(n - 1):
    result += nums[i] * (sums - nums[i])
    sums -= nums[i]
print(result)
