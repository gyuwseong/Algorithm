import sys


def draw_star(n):
    if n == 3:
        return ["  *  ", " * * ", "*****"]

    small_block = draw_star(n // 2)
    pattern = []

    for block in small_block:
        pattern.append(" " * (n // 2) + block + " " * (n // 2))

    for block in small_block:
        pattern.append(block + " " + block)

    return pattern


n = int(sys.stdin.readline().strip())
result = draw_star(n)
print("\n".join(result))
