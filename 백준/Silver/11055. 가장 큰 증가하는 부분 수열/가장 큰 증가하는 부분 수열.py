import sys

n = int(sys.stdin.readline().strip())
lst = list(map(int, sys.stdin.readline().split()))
dp = lst[:]

for i in range(n):
    for j in range(i):
        if lst[j] < lst[i]:
            dp[i] = max(dp[i], dp[j] + lst[i])

print(max(dp))