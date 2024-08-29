'''
h = []
heapq.heappush(h,tmp)
heapq.heappop(h)

작은 숫자부터 높은 우선순위 (오름차순) / O(NlogN)
'''


import sys
import heapq


n = int(sys.stdin.readline())
sch = []
for _ in range(n):
    sch.append(list(map(int, sys.stdin.readline().split())))

sch.sort()

h = []
heapq.heappush(h,sch[0][1])
for i in sch[1:]:
    if h[0] > i[0]:
        heapq.heappush(h,i[1])
    else:
        heapq.heappop(h)
        heapq.heappush(h,i[1])
print(len(h))

