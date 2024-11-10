import sys

n = int(sys.stdin.readline().strip())
nums = sorted(list(map(int, sys.stdin.readline().split())))
target = int(sys.stdin.readline().strip())

start = 0
end = n - 1
cnt = 0

while start < end:
    if nums[start] + nums[end] == target:
        cnt += 1
        start += 1
        end -= 1
    elif nums[start] + nums[end] > target:
        end -= 1
    else:
        start += 1
print(cnt)