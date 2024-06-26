import sys

m = int(sys.stdin.readline())

s = set()
for _ in range(m):
    lst = list(sys.stdin.readline().split())
    w = lst[0]
    if w == "add":
        s.add(int(lst[1]))
    elif w == "check":
        if int(lst[1]) in s:
            print(1)
        else:
            print(0)
    elif w == "remove":
        if int(lst[1]) in s:
            s.remove(int(lst[1]))
    elif w == "toggle":
        if int(lst[1]) in s:
            s.remove(int(lst[1]))
        else:
            s.add(int(lst[1]))
    elif w == "all":
        tmp = [i for i in range(1, 21)]
        s = set(tmp)
    elif w == "empty":
        s = set()