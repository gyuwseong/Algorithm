import sys
import collections

n, m, r = map(int, sys.stdin.readline().split())
graph = list([] for _ in range(n + 1))
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

for g in graph:
    g.sort()

visited = [0] * (n + 1)
count = 1


def bfs(x):
    q = collections.deque([x])
    global count
    visited[x] = count
    count += 1
    while q:
        a = q.popleft()
        for i in graph[a]:
            if not visited[i]:
                q.append(i)
                visited[i] = count
                count += 1


bfs(r)

for i in range(1, n + 1):
    print(visited[i])