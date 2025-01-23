import sys

n, m = map(int, sys.stdin.readline().split())
nums = sorted(list(map(int, sys.stdin.readline().split())))


def dfs(arr, start):
    if len(arr) == m:
        print(*arr)
        return

    before = 0
    for i in range(start, n):
        if nums[i] != before:
            dfs(arr + [nums[i]], i)
            before = nums[i]


dfs([], 0)
