import sys

n, k = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))

start = 0
min_len = n + 1
count = 0

for end in range(n):
    if nums[end] == 1:
        count += 1

    while count >= k:
        min_len = min(end - start + 1, min_len)
        if nums[start] == 1:
            count -= 1
        start += 1

if min_len == n + 1:
    print(-1)
else:
    print(min_len)
