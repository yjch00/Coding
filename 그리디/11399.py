import sys

n = int(sys.stdin.readline())

minutes = list(map(int, sys.stdin.readline().split()))
minutes.sort()


total = []

tmp = 0

for i in minutes:
    tmp += i
    total.append(tmp)
print(sum(total)) 