import sys
import collections

n = int(sys.stdin.readline().strip())
m = int(sys.stdin.readline().strip())

graph = [[False] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a][b] = True
    graph[b][a] = True

bfs_visited = [False] * (n + 1)


def bfs(v):
    q = collections.deque([v])
    bfs_visited[v] = True
    while q:
        v = q.popleft()
        for i in range(n + 1):
            if not bfs_visited[i] and graph[v][i]:
                q.append(i)
                bfs_visited[i] = True


bfs(1)
print(bfs_visited.count(True) - 1)