import sys
K = int(sys.stdin.readline())

stack = []
for _ in range(K):
    num = int(sys.stdin.readline())
    if stack and num == 0:
        stack.pop()
    else:
        stack.append(num)

print(sum(stack))
