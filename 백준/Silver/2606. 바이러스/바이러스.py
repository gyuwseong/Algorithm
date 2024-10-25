import sys

n = int(sys.stdin.readline().strip())
m = int(sys.stdin.readline().strip())

graph = [[False] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a][b] = True
    graph[b][a] = True

dfs_visited = [False] * (n + 1)


def dfs(v):
    dfs_visited[v] = True
    for i in range(1, n + 1):
        if not dfs_visited[i] and graph[v][i]:
            dfs(i)


dfs(1)
print(dfs_visited.count(True) - 1)
