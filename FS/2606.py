import sys
from collections import deque
n = int(sys.stdin.readline())
if n == 1:
    print(0)
    exit()
m = int(sys.stdin.readline())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)


def bfs(start):
    queue = deque([start])
    visited[start] = True
    while queue:
        node = queue.popleft()
        for i in graph[node]:
            if visited[i] == False:
                visited[i] = True
                queue.append(i)
    


visited = [False for _ in range(n+1)]
bfs(1)
print(sum(visited) - 1)