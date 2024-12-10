import sys

n = int(sys.stdin.readline().strip())
nums = sorted(list(map(int, sys.stdin.readline().split())))

start, end, min_value = 0, n - 1, float('inf')
result = set()

while start < end:
    current_sum = nums[start] + nums[end]

    if abs(current_sum) < abs(min_value):
        min_value = current_sum
        result = (nums[start], nums[end])

    if current_sum < 0:
        start += 1
    elif current_sum > 0:
        end -= 1
    else:
        break

print(*result)
