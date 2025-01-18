import sys

n, m = map(int, sys.stdin.readline().split())
nums = sorted(list(map(int, sys.stdin.readline().split())))

visited = [False] * n


def dfs(arr):
    if len(arr) == m:
        print(*arr)
        return

    before = 0
    for i in range(n):
        if not visited[i] and nums[i] != before:
            visited[i] = True
            dfs(arr + [nums[i]])
            visited[i] = False
            before = nums[i]


dfs([])
