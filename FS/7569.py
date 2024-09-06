import sys
from collections import deque

m, n, h = map(int, sys.stdin.readline().split())

maps = [[[] for _ in range(h)] for __ in range(n)]
for i in range(h):
    for j in range(n):
        maps[j][i] = list(map(int, sys.stdin.readline().split()))

# print(maps[1][1])  # n-1 -> h-1 -> m-1순서

start_node = []
for i in range(n):
    for j in range(h):
        for k in range(m):
            if maps[i][j][k] == 1:
                start_node.append([i,j,k]) 
# print(start_node)

ans = 0
def bfs(v):
    global ans
    queue = deque(v)
    while queue:
        x,y,z = queue.popleft()
        dx = [0, 0, -1, 1,0,0]
        dy = [-1, 1, 0, 0,0,0]
        dz = [0,0,0,0,-1,1]
        for ddx, ddy, ddz in zip(dx, dy, dz):
            new_x, new_y, new_z = x+ddx, y+ddy, z+ddz
            if new_x < 0 or new_y < 0 or new_z < 0 or new_x >= n or new_y >=h or new_z >= m:
                continue
        
            if maps[new_x][new_y][new_z] == 0:
                maps[new_x][new_y][new_z] = maps[x][y][z] + 1
                ans = max(ans, maps[new_x][new_y][new_z])
                queue.append([new_x, new_y, new_z])

iszero = False
for i in range(n):
    for j in range(h):
        for k in range(m):
            if maps[i][j][k] == 0:
                iszero = True 
if not iszero:
    print(0)
    exit()

bfs(start_node)
iszero = False
for i in range(n):
    for j in range(h):
        for k in range(m):
            if maps[i][j][k] == 0:
                iszero = True 
print(-1 if iszero else ans-1)