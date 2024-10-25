import sys
import collections

n, m, v = map(int, sys.stdin.readline().split())
graph = [[False] * (n + 1) for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a][b] = True
    graph[b][a] = True

dfs_visited = [False] * (n + 1)
bfs_visited = [False] * (n + 1)


def dfs(v):
    dfs_visited[v] = True
    print(v, end=" ")
    for i in range(1, n + 1):
        if not dfs_visited[i] and graph[v][i]:
            dfs(i)


def bfs(v):
    q = collections.deque([v])
    bfs_visited[v] = True
    while q:
        v = q.popleft()
        print(v, end=" ")
        for i in range(1, n + 1):
            if not bfs_visited[i] and graph[v][i]:
                q.append(i)
                bfs_visited[i] = True


dfs(v)
print()
bfs(v)
