import sys

n, m = map(int, sys.stdin.readline().split())
init_nums = sorted(map(int, sys.stdin.readline().split()))

visited = [False] * n


def dfs(start, nums):
    if start == m:
        print(*nums)
        return

    for i in range(n):
        if not visited[i]:
            visited[i] = True
            dfs(start + 1, nums + [init_nums[i]])
            visited[i] = False


dfs(0, [])
