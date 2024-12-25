import collections
import sys

n = int(sys.stdin.readline().strip())
places = list(list(sys.stdin.readline().strip()) for _ in range(n))

visited_bfs_first = set()
count_first = 0
visited_bfs_second = set()
count_second = 0
direcs = [[1, 0], [-1, 0], [0, 1], [0, -1]]


# 적록색약 O
def bfs_first(a, b):
    q = collections.deque([(a, b)])
    visited_bfs_first.add((a, b))
    while q:
        x, y = q.popleft()
        for dx, dy in direcs:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and (nx, ny) not in visited_bfs_first:
                if (places[x][y] in {"R", "G"} and places[nx][ny] in {"R", "G"}) or (
                        places[x][y] == "B" and places[nx][ny] == "B"):
                    q.append((nx, ny))
                    visited_bfs_first.add((nx, ny))


for i in range(n):
    for j in range(n):
        if (i, j) not in visited_bfs_first:
            bfs_first(i, j)
            count_first += 1


# 적록색약 X
def bfs_second(a, b):
    q = collections.deque([(a, b)])
    visited_bfs_second.add((a, b))
    while q:
        x, y = q.popleft()
        for dx, dy in direcs:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and (nx, ny) not in visited_bfs_second and places[x][y] == places[nx][ny]:
                visited_bfs_second.add((nx, ny))
                q.append((nx, ny))


for i in range(n):
    for j in range(n):
        if (i, j) not in visited_bfs_second:
            bfs_second(i, j)
            count_second += 1

print(count_second, end=" ")
print(count_first)
