import sys
from collections import deque

n = int(sys.stdin.readline())
maps = []
for _ in range(n):
    tmp = sys.stdin.readline().strip()
    maps.append(list(map(int, list(tmp))))
# print(maps)




def bfs(v):
    global cnt
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    queue = deque([v])
    while queue:
        x,y = queue.popleft()
        for i, j in zip(dx, dy):
            new_x = x+i
            new_y = y+j
            if new_x<0 or new_y<0 or new_x>=n or new_y>=n:
                continue
            if maps[new_x][new_y] == 1 and ([new_x, new_y] != v):
                maps[new_x][new_y] = maps[x][y] + 1
                queue.append([new_x, new_y])
                cnt += 1

ans = []
for i in range(n):
    for j in range(n):
        if maps[i][j] == 1:
            cnt = 1
            bfs([i,j])
            ans.append(cnt)
ans.sort()
print(len(ans))
for i in ans:
    print(i)