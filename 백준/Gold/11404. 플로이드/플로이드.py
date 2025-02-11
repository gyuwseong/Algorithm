import sys

n = int(sys.stdin.readline().strip())
m = int(sys.stdin.readline().strip())
rst = [list([int(1e9)] * n) for _ in range(n)]

for i in range(n):
    rst[i][i] = 0

for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    a -= 1
    b -= 1
    rst[a][b] = min(rst[a][b], c)

for k in range(n):
    for i in range(n):
        for j in range(n):
            rst[i][j] = min(rst[i][j], rst[i][k] + rst[k][j])

for _ in rst:
    print(*[0 if x == int(1e9) else x for x in _])
