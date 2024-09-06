import sys
from collections import deque

n, m, v = map(int, sys.stdin.readline().split())


## dfs
visited1 = [False] * (n+1)
visited2 = [False] * (n+1)

graph = [[] for _ in range(n+1)]
for i in range(m):
    a,b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
for i in range(1,n+1):
    graph[i].sort()

def dfs(v):  # dfs는 재귀로 구현
  visited1[v] = True        
  print(v, end = " ")
  for i in range(1, n + 1):
    if (visited1[i] == False) and (i in graph[v]):
      dfs(i)


def bfs(v):
    queue = deque([])
    queue.append(v)
    while queue:
        node = queue.popleft()
        if not visited2[node]:
            visited2[node] = True
            queue.extend(graph[node])
            print(node, end=' ')
    


dfs(v)
print()
bfs(v)
