import sys

t = int(sys.stdin.readline().strip())
nums = list(int(sys.stdin.readline().strip()) for _ in range(t))

dp = [0] * 101
dp[1:3] = [1, 1]
for i in range(3, 101):
    dp[i] = dp[i - 2] + dp[i - 3]

for n in nums:
    print(dp[n])