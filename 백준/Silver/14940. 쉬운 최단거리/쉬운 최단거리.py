import collections
import sys

n, m = map(int, sys.stdin.readline().split())
places = list(list(map(int, sys.stdin.readline().split())) for _ in range(n))
result = list([-1] * m for _ in range(n))
direcs = [[1, 0], [-1, 0], [0, 1], [0, -1]]


def bfs(a, b):
    q = collections.deque([(a, b)])
    while q:
        x, y = q.popleft()
        for dx, dy in direcs:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and result[nx][ny] == -1:
                if places[nx][ny] == 0:
                    result[nx][ny] = 0
                elif places[nx][ny] == 1:
                    result[nx][ny] = result[x][y] + 1
                    q.append((nx, ny))


for i in range(n):
    for j in range(m):
        if places[i][j] == 2:
            result[i][j] = 0
            bfs(i, j)

for i in range(n):
    for j in range(m):
        if places[i][j] == 0:
            result[i][j] = 0
        print(result[i][j], end=" ")
    print()
