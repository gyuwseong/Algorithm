import collections


def solution(maps):
    def bfs(a, b, maps):
        n = len(maps)
        m = len(maps[0])
        q = collections.deque([(a, b, 1)])
        visited = set()
        direcs = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        while q:
            x, y, cnt = q.popleft()
            visited.add((x, y))

            if x == n - 1 and y == m - 1:
                return cnt

            for dx, dy in direcs:
                nx, ny = dx + x, dy + y
                if 0 <= nx < n and 0 <= ny < m and (nx, ny) not in visited and maps[nx][ny] == 1:
                    q.append((nx, ny, cnt + 1))
                    visited.add((nx, ny))

        return -1

    return bfs(0, 0, maps)