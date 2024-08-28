import sys

n = int(sys.stdin.readline())
ropes = []
for _ in range(n):
    ropes.append(int(sys.stdin.readline()))


ropes.sort()

total = ropes[0]*n
for idx in range(1,n):
    
    total = max(total, ropes[idx]*(n-idx))
print(total)
    
