import sys

n = int(sys.stdin.readline().strip())
nums = list(map(int, sys.stdin.readline().split()))

current_sum = nums[0]
max_sum = nums[0]

for i in range(1, n):
    current_sum = max(current_sum + nums[i], nums[i])
    max_sum = max(max_sum, current_sum)
print(max_sum)