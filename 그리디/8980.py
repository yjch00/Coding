'''
무조건 최대한 빨리 내릴 수 있는 애부터 채우는 게 좋다 => yes
capa관점으로 접근! 


'''


import sys
from collections import deque
n, c = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
info = []
for _ in range(m):
    s, f, box = map(int, sys.stdin.readline().split())
    info.append((s, f, box))
info.sort(key=lambda x: (x[1]))

capa = [c] * n
total = 0
for s, f, box in info: # start, finish, box
    _min = c        # 초기값
    for i in range(s,f):
        _min = min(_min, capa[i])      # start ~ finish 전까지 최대 capa 구하기 (min값이 최대 capa)
    min_now = min(_min, box)            # capa랑 지금 box의 수 중 더 작은 수를 선택
    for i in range(s,f):
        capa[i] -= min_now
    total += min_now
print(total)



