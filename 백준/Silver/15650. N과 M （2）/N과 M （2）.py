import sys

n, m = map(int, sys.stdin.readline().split())


def dfs(nums, start, n, m):
    if len(nums) == m:
        print(*nums)
        return

    for i in range(start, n + 1):
        dfs(nums + [i], i + 1, n, m)


dfs([], 1, n, m)
