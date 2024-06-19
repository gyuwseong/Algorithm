import sys

n = int(sys.stdin.readline())
lst = [int(sys.stdin.readline()) for i in range(n)]
start = 0
st = []
i = 1
rst = []
while start < n:
    if not st:
        st.append(i)
        rst.append("+")
        i += 1
    elif st[-1] == lst[start]:
        st.pop()
        rst.append("-")
        start += 1
    elif i > n:
        print("NO")
        exit()
    else:
        st.append(i)
        rst.append("+")
        i += 1
for _ in rst:
    print(_)
