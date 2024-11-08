import sys

n = int(sys.stdin.readline().strip())
dp = [0] * 12
dp[1:4] = 1, 2, 4

for i in range(4, 12):
    dp[i] = sum(dp[i - 3: i])

for _ in range(n):
    index = int(sys.stdin.readline().strip())
    print(dp[index])
