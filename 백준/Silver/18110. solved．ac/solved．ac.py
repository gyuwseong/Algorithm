import sys


def n_round(num):
    return int(num) + (1 if num - int(num) >= 0.5 else 0)


n = int(sys.stdin.readline())
if n == 0:
    print(0)
else:
    lst = sorted([int(sys.stdin.readline()) for i in range(n)])
    excl = n_round(n * 0.15)
    print(n_round(sum(lst[excl:n - excl]) / (n - 2 * excl)))