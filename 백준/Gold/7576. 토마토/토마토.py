import collections
import sys

m, n = map(int, sys.stdin.readline().split())
boxes = list(list(map(int, sys.stdin.readline().split())) for _ in range(n))

if all(box != 0 for row in boxes for box in row):
    print(0)
    sys.exit()

q = collections.deque()
for i in range(n):
    for j in range(m):
        if boxes[i][j] == 1:
            q.append((i, j))

count = 0
while q:
    for _ in range(len(q)):
        x, y = q.popleft()
        direcs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        for dx, dy in direcs:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and boxes[nx][ny] == 0:
                q.append((nx, ny))
                boxes[nx][ny] = 1
    count += 1

if any(box == 0 for row in boxes for box in row):
    print(-1)
else:
    print(count - 1)
