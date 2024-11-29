import sys

n = int(sys.stdin.readline().strip())
dp = [0] * 1000001
dp[:3] = [0, 1, 2]

for i in range(3, n + 1):
    dp[i] = (dp[i - 1] + dp[i - 2]) % 15746

print(dp[n])