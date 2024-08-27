# 리스트로 플면 시간초과

# import sys

# n = int(sys.stdin.readline().strip())
# queue = []
# for _ in range(n):
#     next = sys.stdin.readline().strip().split()
#     if next[0] == 'push':
#         queue.append(next[1])
#     elif next[0] == 'pop':
#         if not queue:
#             print(-1)
#         else:
#             print(queue.pop(0))
#     elif next[0] == 'size':
#         print(len(queue))
#     elif next[0] == 'empty':
#         if not queue:
#             print(1)
#         else:
#             print(0)
#     elif next[0] == 'front':
#         if not queue:
#             print(-1)
#         else: print(queue[0])
#     elif next[0] == 'back':
#         if not queue:
#             print(-1)
#         else: print(queue[-1])

from collections import deque
import sys

n = int(sys.stdin.readline().strip())
queue = deque([])
for _ in range(n):
    next = sys.stdin.readline().strip().split()
    if next[0] == 'push':
        queue.append(next[1])
    elif next[0] == 'pop':
        if not queue:
            print(-1)
        else:
            print(queue.popleft())
    elif next[0] == 'size':
        print(len(queue))
    elif next[0] == 'empty':
        if not queue:
            print(1)
        else:
            print(0)
    elif next[0] == 'front':
        if not queue:
            print(-1)
        else: print(queue[0])
    elif next[0] == 'back':
        if not queue:
            print(-1)
        else: print(queue[-1])