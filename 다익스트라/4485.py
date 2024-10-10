import sys
import heapq

INF = 1e8
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
def dij(s_x, s_y):
    q = []
    cost = [[INF]*(n) for _ in range(n)]
    cost[s_x][s_y] = graph[s_x][s_y]
    heapq.heappush(q, (graph[s_x][s_y], s_x, s_y))
    
    while q:
        c, x, y = heapq.heappop(q)
        if x == n-1 and y == n-1:
            print(f'Problem {cnt}:',cost[x][y])
            break
            
        if cost[x][y] < c:
            continue
        for i in range(4):
            new_x, new_y = x+dx[i], y+dy[i]
            if (0 <= new_x < n) and (0 <= new_y < n):
                if cost[new_x][new_y] > c + graph[new_x][new_y]:
                    cost[new_x][new_y] = c + graph[new_x][new_y]
                    heapq.heappush(q, (c + graph[new_x][new_y], new_x, new_y))
    # return cost[n-1][n-1]
                
cnt = 1

while True:
    n = int(sys.stdin.readline())
    if n == 0:
        break
    graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    dij(0,0)
    
    cnt += 1
    