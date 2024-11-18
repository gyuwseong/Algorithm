import sys

k, l = map(int, sys.stdin.readline().split())
student_list = {}

for _ in range(l):
    student = sys.stdin.readline().strip()
    if student in student_list:
        del student_list[student]
    student_list[student] = 1

for k in list(student_list.keys())[:k]:
    print(k)