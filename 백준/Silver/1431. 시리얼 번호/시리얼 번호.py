import sys

n = int(sys.stdin.readline().strip())
input_list = list(sys.stdin.readline().strip() for _ in range(n))
sorted_list = sorted(input_list, key=lambda x: (len(x), sum(int(i) for i in x if i.isdigit()), x))

for _ in sorted_list:
    print(_)