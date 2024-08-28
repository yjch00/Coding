import sys

n, k = map(int, sys.stdin.readline().strip().split())
money = []
total = 0

for _ in range(n):
    money.append(int(sys.stdin.readline().strip()))
for i in money[::-1]:
    if k // i >= 1:
        total += k//i
        k = k % i
print(total)