import sys

n, s = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))

start, end = 0, 0
sums = 0
min_len = 1e9

while True:
    if sums >= s:
        min_len = min(end - start, min_len)
        sums -= nums[start]
        start += 1
    elif end == n:
        break
    else:
        sums += nums[end]
        end += 1

if min_len == 1e9:
    print(0)
else:
    print(min_len)
