import sys

n = int(sys.stdin.readline().strip())
nums = list(map(int, sys.stdin.readline().split()))

result = [-1] * n
stack = []

for i in range(n):
    while stack and nums[stack[-1]] < nums[i]:
        idx = stack.pop()
        result[idx] = nums[i]
    stack.append(i)

print(*result)
