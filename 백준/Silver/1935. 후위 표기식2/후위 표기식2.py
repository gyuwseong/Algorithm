import sys

n = int(sys.stdin.readline().strip())
notation = sys.stdin.readline().strip()
letter_dic = {}
for i in range(65, 65 + n):
    letter_dic[chr(i)] = int(sys.stdin.readline().strip())

stack = []
for j in notation:
    if j in letter_dic:
        stack.append(letter_dic[j])
    else:
        second = stack.pop()
        first = stack.pop()
        if j == "-":
            stack.append(first - second)
        elif j == '+':
            stack.append(first + second)
        elif j == '*':
            stack.append(first * second)
        elif j == '/':
            stack.append(first / second)

print("{:.2f}".format(stack[0]))
