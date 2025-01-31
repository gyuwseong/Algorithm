import sys

n, s = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))
cnt = 0


def dfs(rst, start):
    global cnt
    if sum(rst) == s and len(rst) > 0:
        cnt += 1

    for i in range(start, n):
        dfs(rst + [nums[i]], i + 1)


dfs([], 0)
print(cnt)
