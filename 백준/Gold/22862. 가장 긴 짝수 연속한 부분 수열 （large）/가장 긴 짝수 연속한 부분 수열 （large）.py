import sys

n, k = map(int, sys.stdin.readline().split())
s = list(map(int, sys.stdin.readline().split()))

start = 0
odd_cnt = 0
max_cnt = 0

for end in range(n):
    if s[end] % 2 != 0:
        odd_cnt += 1
    while odd_cnt > k:
        if s[start] % 2 != 0:
            odd_cnt -= 1
        start += 1
    max_cnt = max(max_cnt, end - start + 1 - odd_cnt)

print(max_cnt)