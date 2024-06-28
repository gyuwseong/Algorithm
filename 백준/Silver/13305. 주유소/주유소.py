import sys

n = int(sys.stdin.readline())
length = list(map(int, sys.stdin.readline().split()))
price = list(map(int, sys.stdin.readline().split()))

min_p = price[0]
rst = 0

for i in range(n - 1):
    if min_p > price[i]:
        min_p = price[i]
    rst += min_p * length[i]
print(rst)