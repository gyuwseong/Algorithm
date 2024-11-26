import sys

a, p = map(int, sys.stdin.readline().split())
nums_list = [a]

while True:
    new_num = 0
    for i in str(a):
        new_num += int(i) ** p
    if new_num in nums_list:
        break
    nums_list.append(new_num)
    a = new_num

print(nums_list.index(new_num))