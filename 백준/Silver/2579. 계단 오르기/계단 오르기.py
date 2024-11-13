import sys

n = int(sys.stdin.readline().strip())
numbers = list(int(sys.stdin.readline().strip()) for _ in range(n))

dp1 = [0] * (n + 1)
dp2 = [0] * (n + 1)

if n >= 1:
    dp1[1] = numbers[0]

if n >= 2:
    dp1[2] = numbers[0] + numbers[1]
    dp2[2] = numbers[1]

for i in range(3, n + 1):
    dp1[i] = dp2[i - 1] + numbers[i - 1]
    dp2[i] = max(dp1[i - 2], dp2[i - 2]) + numbers[i - 1]
print(max(dp1[n], dp2[n]))