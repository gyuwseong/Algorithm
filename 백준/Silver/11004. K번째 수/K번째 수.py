import sys

n, k = map(int, sys.stdin.readline().split())
input_list = sorted(list(map(int, sys.stdin.readline().split())))
print(input_list[k - 1])