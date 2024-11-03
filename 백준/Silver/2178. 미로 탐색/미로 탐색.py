import sys
import collections

n, m = map(int, sys.stdin.readline().split())
graph = [[0] * (m + 1)]
for _ in range(n):
    lst = [0] + list(map(int, sys.stdin.readline().strip()))
    graph.append(lst)


def bfs(a, b):
    q = collections.deque([(a, b)])
    v = [[0] * (m + 1) for _ in range(n + 1)]
    v[a][b] = 1

    while q:
        x, y = q.popleft()
        if x == n and y == m:
            return v[x][y]

        direc = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        for dx, dy in direc:
            nx, ny = dx + x, dy + y
            if 1 <= nx < n + 1 and 1 <= ny < m + 1 and v[nx][ny] == 0 and graph[nx][ny] == 1:
                q.append((nx, ny))
                v[nx][ny] = v[x][y] + 1


print(bfs(1, 1))