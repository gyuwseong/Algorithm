import sys


def draw_star(n):
    if n == 1:
        return ["*"]

    small_block = draw_star(n // 3)
    pattern = []

    for block in small_block:
        pattern.append(block * 3)

    for block in small_block:
        pattern.append(block + " " * (n // 3) + block)

    for block in small_block:
        pattern.append(block * 3)

    return pattern


n = int(sys.stdin.readline().strip())
result = draw_star(n)
print("\n".join(result))
