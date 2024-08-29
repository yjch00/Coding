import heapq
import sys

lines = []
n = int(sys.stdin.readline())
for _ in range(n):
    lines.append(list(map(int, sys.stdin.readline().split())))

lines.sort()
h = []

total = -lines[0][0]
first = lines[0][1]
for i in lines[1:]:
    if i[0] <= first:
        first = max(first, i[1])
    else:
        total += first
        total -= i[0]
        first = i[1]
print(total+first)

