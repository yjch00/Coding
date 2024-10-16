import sys


# sys.setrecursionlimit(10**6)

def dfs(start, group):
    visited[start] = group
    for i in graph[start]:
        if visited[i] == 0:
            result = dfs(i, -group)
            if not result:
                return False
        else:
            if visited[i] == group:
                return False
    return True
            


k = int(sys.stdin.readline())
for _ in range(k):
    v, e = map(int, sys.stdin.readline().split())
    graph = [[] for __ in range(v+1)]
    visited = [0] * (v+1)

    for _ in range(e):
        a, b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)

    for i in range(1, v+1):
        if visited[i] == 0:
            result = dfs(i, 1)
            if not result:
                break
    print('YES') if result else print('NO')

