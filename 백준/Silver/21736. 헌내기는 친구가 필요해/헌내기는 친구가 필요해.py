import collections
import sys

n, m = map(int, sys.stdin.readline().split())
places = list(list(sys.stdin.readline().strip()) for _ in range(n))

visited_bfs = set()
count = 0
direcs = [[1, 0], [-1, 0], [0, 1], [0, -1]]


def bfs(a, b):
    global count
    q = collections.deque([(a, b)])
    visited_bfs.add((a, b))
    while q:
        x, y = q.popleft()
        for dx, dy in direcs:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and (nx, ny) not in visited_bfs:
                visited_bfs.add((nx, ny))
                if places[nx][ny] == "X":
                    continue
                elif places[nx][ny] == "P":
                    count += 1
                q.append((nx, ny))


for i in range(n):
    for j in range(m):
        if places[i][j] == "I":
            bfs(i, j)

print(count if count > 0 else "TT")
