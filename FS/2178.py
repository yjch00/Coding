import sys
from collections import deque

n,m = map(int, sys.stdin.readline().split())
maps = []
for _ in range(n):
    tmp = sys.stdin.readline().strip()
    maps.append(list(map(int, list(tmp))))
# print(maps)

def bfs(v):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    queue = deque([v])
    while queue:
        x,y = queue.popleft()
        for i, j in zip(dx, dy):
            new_x = x+i
            new_y = y+j
            if new_x<0 or new_y<0 or new_x>=n or new_y>=m:
                continue
            if maps[new_x][new_y] == 1:
                maps[new_x][new_y] = maps[x][y] + 1
                queue.append([new_x, new_y])
                # print([new_x, new_y])
bfs([0,0])
# for i in range(n):
#     print(' '.join(map(str, maps[i])))
print(maps[n-1][m-1])


