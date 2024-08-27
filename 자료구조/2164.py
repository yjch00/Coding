import sys
from collections import deque

n = int(sys.stdin.readline().strip())
queue = deque(range(1,n+1,1))

while len(queue)>1:
    queue.popleft()
    tmp = queue.popleft()
    queue.append(tmp)
print(queue[0])
