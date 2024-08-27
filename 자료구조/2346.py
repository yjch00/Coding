import sys
from collections import deque

n = int(sys.stdin.readline().strip())
m = list(map(int, sys.stdin.readline().strip().split()))
queue = deque(range(1,n+1,1))

boom = []
idx = 1
while queue:
    print(idx)
    print(queue)

    if idx-1 >= 0:
        for i in range(idx-1):
            queue.append(queue.popleft())
    else:
        for i in range(-idx+1):
            queue.insert(0,queue.pop())
    tmp = queue.popleft()
    boom.append(tmp)
    idx = idx + m[tmp-1] - 1
print(boom)

