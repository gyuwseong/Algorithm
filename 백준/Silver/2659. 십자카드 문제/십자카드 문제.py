import sys
import collections

nums = list(map(int, sys.stdin.readline().split()))


def check_nums(nums):
    min_nums = int(''.join(map(str, nums)))
    q = collections.deque(nums)
    for _ in range(4):
        q.rotate()
        new_nums = int(''.join(map(str, q)))
        min_nums = min(min_nums, new_nums)
    return min_nums


init_nums = check_nums(nums)

count = 0
for i in range(1111, init_nums + 1):
    if "0" not in str(i) and i == check_nums(list(map(int, str(i)))):
        count += 1

print(count)