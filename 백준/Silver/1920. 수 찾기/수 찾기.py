import sys

n = int(sys.stdin.readline())
a_lst = sorted(list(map(int, sys.stdin.readline().split())))
m = int(sys.stdin.readline())
b_lst = list(map(int, sys.stdin.readline().split()))


def binarySearch(lst, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if lst[mid] == target:
        return True
    elif lst[mid] > target:
        return binarySearch(lst, target, 0, mid - 1)
    else:
        return binarySearch(lst, target, mid + 1, end)


for l in b_lst:
    result = binarySearch(a_lst, l, 0, n - 1)
    if not result:
        print(0)
    else:
        print(1)