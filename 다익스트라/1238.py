# import sys

# n, m, x = map(int, sys.stdin.readline().split())
# graph = [[] for _ in range(n+1)]
# INF = 1e8
# for _ in range(m):
#     a, b, t = map(int, sys.stdin.readline().split())
#     graph[a].append((b,t)) # 도착노드, 소모시간
    

# import heapq
# def dij(start):
#     q = []
#     distance = [INF]*(n+1) 
    
    
#     distance[start] = 0
#     heapq.heappush(q, (0, start)) # 시간, 노드 순서
#     while q:
#         # print(distance)
#         dist, now = heapq.heappop(q)
#         if distance[now] < dist:  #이미 해당 노드가 업데이트 되어 있는 경우
#             continue
        
#         for i in graph[now]:
#             if i[1] + dist < distance[i[0]]:
#                 distance[i[0]] = i[1] + dist
#                 heapq.heappush(q, (i[1]+dist, i[0]))
#     return distance
                
# result = 0
# back = dij(x)  # 파티에서 출발
# for i in range(1,n+1):
#     go = dij(i) # 집에서 출발
#     result = max(result, go[x] + back[i]) #각각 파티 도착, 집 도착
# print(result)
        
        
import sys

n, m, x = map(int, sys.stdin.readline().split())
go_graph = [[] for _ in range(n+1)]
back_graph = [[] for _ in range(n+1)]

INF = 1e6
for _ in range(m):
    a, b, t = map(int, sys.stdin.readline().split())
    go_graph[a].append((b,t)) # 도착노드, 소모시간
    back_graph[b].append((a,t))

import heapq
def dij(start,graph, n):
    q = []
    distance = [INF]*(n+1) 
    
    
    distance[start] = 0
    heapq.heappush(q, (0, start)) # 시간, 노드 순서
    while q:
        # print(distance)
        dist, now = heapq.heappop(q)
        if distance[now] < dist:  #이미 해당 노드가 업데이트 되어 있는 경우
            continue
        
        for i in graph[now]:
            if i[1] + dist < distance[i[0]]:
                distance[i[0]] = i[1] + dist
                heapq.heappush(q, (i[1]+dist, i[0]))
    return distance
                
result = 0
go_distance = dij(x, go_graph, n)
back_distance = dij(x, back_graph, n)
for i in range(1,n+1):
    total_time = go_distance[i]+back_distance[i]
    result = max(result, total_time)
print(result)
        