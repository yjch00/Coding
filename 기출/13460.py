import sys


n,m = map(int, sys.stdin.readline().split())

maps = []
for _ in range(n):
    tmp = sys.stdin.readline().strip()
    maps.append(list(tmp))
print(maps)