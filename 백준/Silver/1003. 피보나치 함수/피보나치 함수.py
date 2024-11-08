import sys

t = int(sys.stdin.readline().strip())
nums = list(int(sys.stdin.readline().strip()) for _ in range(t))
end = max(nums) + 1
dp = [(0, 0)] * end
dp[:2] = [(1, 0), (0, 1)]

for i in range(2, end):
    dp[i] = tuple(a + b for a, b in zip(dp[i - 2], dp[i - 1]))

for n in nums:
    print(f'{dp[n][0]} {dp[n][1]}')