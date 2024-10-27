import sys
import collections

n, m = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

bfs_visited = [False] * (n + 1)
cnt = 0


def bfs(v):
    bfs_visited[v] = True
    q = collections.deque([v])
    while q:
        a = q.popleft()
        for i in graph[a]:
            if not bfs_visited[i]:
                q.append(i)
                bfs_visited[i] = True


for i in range(1, n + 1):
    if not bfs_visited[i]:
        bfs(i)
        cnt += 1

print(cnt)
