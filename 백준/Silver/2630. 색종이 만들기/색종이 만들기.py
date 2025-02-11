import sys

n = int(sys.stdin.readline().strip())
paper = list(list(map(int, sys.stdin.readline().split())) for _ in range(n))
white, blue = 0, 0


def check(x, y, size):
    global white, blue
    target = paper[x][y]
    for i in range(x, x + size):
        for j in range(y, y + size):
            if target != paper[i][j]:
                new_size = size // 2
                check(x, y, new_size)
                check(x, y + new_size, new_size)
                check(x + new_size, y, new_size)
                check(x + new_size, y + new_size, new_size)
                return

    if target == 1:
        blue += 1
    else:
        white += 1


check(0, 0, n)
print(white)
print(blue)
