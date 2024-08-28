import sys
from collections import deque

n = int(sys.stdin.readline().strip())
m = list(map(int, sys.stdin.readline().strip().split()))
queue = deque(range(1,n+1,1))

boom = []
idx = 1
while queue:
    # print(idx)
    # print(queue)

    if idx-1 >= 0:
        for i in range(idx-1):
            queue.append(queue.popleft())
    else:
        for i in range(-idx):
            queue.insert(0,queue.pop())
    # print(queue)
    tmp = queue.popleft()
    boom.append(str(tmp))
    # print(boom)
    idx = m[tmp-1]
print(' '.join(boom))

