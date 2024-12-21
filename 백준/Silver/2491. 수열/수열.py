import sys

n = int(sys.stdin.readline().strip())
nums = list(map(int, sys.stdin.readline().split()))

dp1 = [1] * n
dp2 = [1] * n

for i in range(n - 1):
    if nums[i + 1] >= nums[i]:
        dp1[i + 1] += dp1[i]

for i in range(n - 1):
    if nums[i + 1] <= nums[i]:
        dp2[i + 1] += dp2[i]

max1 = max(dp1)
max2 = max(dp2)
print(max(max1, max2))
