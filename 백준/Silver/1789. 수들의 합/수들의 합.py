import sys

s = int(sys.stdin.readline())

i = 1
cnt = 0

while True:
    s -= i
    cnt += 1
    i += 1
    if s < 0:
        print(cnt - 1)
        break