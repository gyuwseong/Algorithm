import sys

n = int(sys.stdin.readline().strip())
m = int(sys.stdin.readline().strip())
s = sys.stdin.readline().strip()

start = 0
count = 0
target_count = 0

while start < m - 1:
    if s[start:start + 3] == "IOI":
        target_count += 1
        if target_count >= n:
            count += 1
        start += 2
    else:
        target_count = 0
        start += 1
print(count)