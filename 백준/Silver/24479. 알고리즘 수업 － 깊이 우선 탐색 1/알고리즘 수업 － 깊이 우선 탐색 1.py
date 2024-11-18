import sys

sys.setrecursionlimit(150000)

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


def dfs(x):
    global count
    visited[x] = count
    count += 1
    for i in graph[x]:
        if not visited[i]:
            dfs(i)


dfs(r)

for i in range(1, n + 1):
    print(visited[i])
