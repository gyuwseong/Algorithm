import sys

x = int(sys.stdin.readline().strip())
i = 1

while i < x:
    x -= i
    i += 1
level = i

if not level % 2:
    a, b = x, level - x + 1
else:
    a, b = level - x + 1, x
    
print(f"{a}/{b}")
