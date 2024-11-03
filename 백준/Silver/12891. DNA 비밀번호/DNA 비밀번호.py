import sys

s, p = map(int, sys.stdin.readline().split())
ps = list(sys.stdin.readline().strip())
A, C, G, T = map(int, sys.stdin.readline().split())

initial_target = ps[:p]
target_dic = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
for i in initial_target:
    target_dic[i] += 1

i, cnt = 0, 0
gap = s - p
while p <= s:
    if target_dic["A"] >= A and target_dic["C"] >= C and target_dic["G"] >= G and target_dic["T"] >= T:
        cnt += 1

    i += 1
    p += 1

    if p > s:
        break

    delete = ps[i - 1]
    add = ps[p - 1]

    if target_dic[delete]:
        target_dic[delete] -= 1
    target_dic[add] += 1

print(cnt)
