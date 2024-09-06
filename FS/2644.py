import sys
from collections import deque
n = int(sys.stdin.readline())
a, b = map(int, sys.stdin.readline().split())

m = int(sys.stdin.readline())
visit = [False] * (n+1)
graph = [[] for _ in range(n+1)]
for _ in range(m):
    c,d = map(int, sys.stdin.readline().split())
    graph[c].append(d)
    graph[d].append(c)
    graph[c].sort()
    graph[d].sort()
res = [0] *(n+1)


# # bfs 로 풀기
# def bfs(v):
#     global res
#     queue = deque([v])
#     while queue:
#         node = queue.popleft()
#         for i in graph[node]:
#             if not visit[i]:
#                 visit[i] = True
#                 queue.append(i)
#                 res[i] = res[node] + 1
                

# bfs(a)
# print(res[b] if res[b] != 0 else -1)

# dfs 로 풀기
def dfs(v):
    for i in graph[v]:
        if not visit[i]:
            res[i] = res[v] + 1
            visit[i] = True
            dfs(i)
dfs(a)
print(res[b] if res[b] != 0 else -1)