import sys

n, m, p = map(int, sys.stdin.readline().split())

if n == 0:
    print(1)
else:
    nums = list(map(int, sys.stdin.readline().split()))
    if n >= p and (nums and m <= nums[-1]):
        print(-1)
    else:
        print(len([i for i in nums if i > m]) + 1)