import sys

n, k = map(int, sys.stdin.readline().split())
ppl = list(sys.stdin.readline().strip())

cnt = 0
start = 0
for i in range(n):
    if ppl[i] == "P":
        for j in range(max(i - k, 0), min(i + k + 1, n)):
            if ppl[j] == "H":
                ppl[j] = 1
                cnt += 1
                break
print(cnt)
