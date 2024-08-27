import sys
from collections import deque


queue = deque([])
n = int(sys.stdin.readline().strip())
for _ in range(n):
    m = list(map(int, sys.stdin.readline().strip().split()))
    if m[0] == 1:
        queue.insert(0,m[1])
    elif m[0] == 2:
        queue.append(m[1])
    elif m[0] == 3:
        if not queue:
            print(-1)
        else:
            print(queue.popleft())
    elif m[0] == 4:
        if not queue:
            print(-1)
        else:
            print(queue.pop())
    elif m[0] == 5:
        print(len(queue))
    elif m[0] == 6:
        if not queue:
            print(1)
        else:
            print(0)
    elif m[0] == 7:
        if not queue:
            print(-1)
        else: print(queue[0])
    elif m[0] == 8:
        if not queue:
            print(-1)
        else: print(queue[-1])
    


