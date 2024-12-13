import sys

word = sys.stdin.readline().strip()
target = sys.stdin.readline().strip()

stack = []
target_len = len(target)
for w in word:
    stack.append(w)
    if len(stack) >= target_len:
        if "".join(stack[-target_len:]) == target:
            del stack[-target_len:]

if not stack:
    print("FRULA")
else:
    print("".join(stack))
