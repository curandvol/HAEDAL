import sys
from collections import deque

N = int(sys.stdin.readline())
dq = deque([])

for i in range(N):
    input_str = sys.stdin.readline().split()
    order = input_str[0]
    
    if order == "push":
        dq.append(input_str[1])
    elif order == "pop":
        if len(dq) > 0:
            tmp = dq.popleft()
            print(tmp)
        else:
            print(-1)
    elif order == "size":
        print(len(dq))
    elif order == "empty":
        if len(dq) > 0:
            print(0)
        else:
            print(1)
    elif order == "front":
        if len(dq) > 0:
            print(dq[0])
        else:
            print(-1)
    elif order == "back":
        if len(dq) > 0:
            print(dq[-1])
        else:
            print(-1)
