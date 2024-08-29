
'''

list a 를 heapq로 만드는 방법 : heapq.heapify(a)
'''


import sys
import heapq


n,m = list(map(int, sys.stdin.readline().split()))
a = list(map(int, sys.stdin.readline().split()))

heapq.heapify(a)
for _ in range(m):
    num1 = heapq.heappop(a)
    num2 = heapq.heappop(a)
    heapq.heappush(a,num1+num2)
    heapq.heappush(a,num1+num2)
print(sum(a))