import collections
import sys

direcs = [[1, 0], [-1, 0], [0, 1], [0, -1], [1, 1], [-1, -1], [1, -1], [-1, 1]]

while True:
    w, h = map(int, sys.stdin.readline().split())
    if w == 0 and h == 0:
        break
    if w == 1 and h == 1:
        print(int(sys.stdin.readline().strip()))
        continue

    places = list(list(map(int, sys.stdin.readline().split())) for _ in range(h))
    visited_bfs = set()
    count = 0


    def bfs(a, b):
        q = collections.deque([(a, b)])
        visited_bfs.add((a, b))
        while q:
            x, y = q.popleft()
            for dx, dy in direcs:
                nx, ny = x + dx, y + dy
                if 0 <= nx < h and 0 <= ny < w and (nx, ny) not in visited_bfs and places[nx][ny] == 1:
                    visited_bfs.add((nx, ny))
                    q.append((nx, ny))


    for i in range(h):
        for j in range(w):
            if places[i][j] == 1 and (i, j) not in visited_bfs:
                bfs(i, j)
                count += 1

    print(count)
