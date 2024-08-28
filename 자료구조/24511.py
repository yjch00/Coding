# 스택은 볼 필요가 없다!!!!! (그냥 건너뛰기만 하니까!)


import sys
from collections import deque

n = sys.stdin.readline().strip()
a = sys.stdin.readline().strip().split()
b = sys.stdin.readline().strip().split()
m = sys.stdin.readline().strip()
c = sys.stdin.readline().strip().split()


# output = []
# for i in c: # 2 4 7
#     tmp = i
#     for idx, j in enumerate(a): # 0 1 1 0
#         if j == '0':
#             tmp, b[idx] = b[idx], tmp
            
#         else:
#             continue
#     output.append(tmp)
# print(' '.join(output))
output = []
queue = deque([])
for i, j in zip(a,b):
    if i == '0':
        queue.append(j)

for i in c:
    queue.insert(0,i)
    output.append(queue.pop())
print(' '.join(output))