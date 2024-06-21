import sys

nums = sorted([int(i) for i in sys.stdin.readline().strip()], reverse=True)
if 0 in nums and sum(nums) % 3 == 0:
    print(int("".join(map(str, nums))))
else:
    print(-1)