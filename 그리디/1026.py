import sys

n = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
B = list(map(int, sys.stdin.readline().split()))

A.sort(reverse=True)
B.sort()



total = 0
for a, b in zip(A,B):
    total += a * b
print(total)