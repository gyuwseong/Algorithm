import sys

n, m = map(int, (sys.stdin.readline().split()))
nums = list(map(int, (sys.stdin.readline().split())))

dp = [0] * (n + 1)
for i in range(1, n + 1):
    dp[i] = dp[i - 1] + nums[i - 1]

for _ in range(m):
    x, y = map(int, (sys.stdin.readline().split()))
    print(dp[y] - dp[x - 1])