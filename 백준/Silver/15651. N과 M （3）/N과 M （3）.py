import sys

n, m = map(int, sys.stdin.readline().split())


def dfs(nums):
    if len(nums) == m:
        print(*nums)
        return

    for i in range(1, n + 1):
        dfs(nums + [i])


dfs([])
