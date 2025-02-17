import sys

n = int(sys.stdin.readline().strip())
dp = [0] * (n + 1)
dp[:3] = [0, 1, 3]

for i in range(3, n + 1):
    dp[i] = dp[i - 1] + 2 * dp[i - 2]

print(dp[n] % 10007)