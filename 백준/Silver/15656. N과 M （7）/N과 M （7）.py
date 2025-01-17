import sys

n, m = map(int, sys.stdin.readline().split())
nums = sorted(list(map(int, sys.stdin.readline().split())))


def dfs(arr):
    if len(arr) == m:
        print(*arr)
        return

    for i in range(n):
        dfs(arr + [nums[i]])


dfs([])
