import sys

n, m = map(int, sys.stdin.readline().split())
nums = sorted(list(map(int, sys.stdin.readline().split())))


def dfs(arr, start):
    if len(arr) == m:
        print(*arr)
        return

    for i in range(start, n):
        dfs(arr + [nums[i]], i + 1)


dfs([], 0)
