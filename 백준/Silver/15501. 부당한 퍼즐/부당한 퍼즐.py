import sys

n = int(sys.stdin.readline().strip())
input_list = ' '.join(sys.stdin.readline().split())
double_list = input_list + ' ' + input_list
target_list = ' '.join(sys.stdin.readline().split())
reverse_target_list = ' '.join(target_list.split()[::-1])

if target_list in double_list or reverse_target_list in double_list:
    print("good puzzle")
else:
    print("bad puzzle")
