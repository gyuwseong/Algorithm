import sys

n = int(sys.stdin.readline())
length = list(map(int, sys.stdin.readline().split()))
price = list(map(int, sys.stdin.readline().split()))

min_p = min(price)
i = 0
rst = 0
while i < n:
    if price[i] == min_p:
        rst = price[i] * sum(length)
        print(rst)
        break
    else:
        if price[i] > max(price[i + 1:]):
            rst += price[i] * length[i]
            i += 1
        else:
            rst += price[i] * sum(length[i:])
            print(rst)
            break