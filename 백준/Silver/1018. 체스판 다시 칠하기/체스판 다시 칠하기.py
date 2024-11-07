import sys

n, m = map(int, sys.stdin.readline().split())
input_board = [sys.stdin.readline().strip() for _ in range(n)]

w = 'W', 'B'
b = 'B', 'W'


def check(i, j):
    count_w = 0
    count_b = 0
    for ri in range(8):
        for rj in range(8):
            ni = ri + i
            nj = rj + j
            if input_board[ni][nj] != b[(ri + rj) % 2]:
                count_b += 1

            if input_board[ni][nj] != w[(ri + rj) % 2]:
                count_w += 1

    return min(count_b, count_w)


result = 100000
for k in range(n - 7):
    for l in range(m - 7):
        result = min(result, check(k, l))

print(result)
