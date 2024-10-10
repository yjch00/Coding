import sys

n = int(sys.stdin.readline())
graph = [[' ']*(2*n) for _ in range(n)]

def solution(x,y,N):
    if N == 3:
        graph[x][y] = '*'
        graph[x+1][y-1] = '*'
        graph[x+1][y+1] = '*'
        for i in range(-2,3):
            graph[x+2][y+i] = '*'
    else:
        next_n = N//2               # 12 6 3 
        solution(x, y, next_n)
        solution(x+next_n, y-next_n, next_n)
        solution(x+next_n, y+next_n, next_n)

solution(0,n-1,n)        

for i in graph:
    print(''.join(i))