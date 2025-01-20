import sys

n, m = map(int, sys.stdin.readline().split())
nums = sorted(list(map(int, sys.stdin.readline().split())))

visited = [False] * n


def dfs(arr, start):
    if len(arr) == m:
        print(*arr)
        return

    before = 0
    for i in range(n):
        if nums[i] != before:
            dfs(arr + [nums[i]], start + 1)
            before = nums[i]


dfs([], 0)
