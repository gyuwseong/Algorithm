import collections
import sys

t = int(sys.stdin.readline().strip())
for _ in range(t):
    demand = list(sys.stdin.readline().strip())
    n = int(sys.stdin.readline().strip())
    nums = list(sys.stdin.readline().strip()[1:-1].split(','))
    q = collections.deque(nums)

    if n == 0:
        q = []

    reverse = False
    for d in demand:
        if d == "R":
            reverse = not reverse
        else:
            if not q:
                print("error")
                break
            else:
                if reverse:
                    q.pop()
                else:
                    q.popleft()
    else:
        if reverse:
            q.reverse()
        print('[' + ','.join(q) + ']')
