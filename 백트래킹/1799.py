'''
(0,0) (0,1)
(1,0) (1,1)

우상향 그래프는 r+c 가 동일하다
우하향 그래프는 r-c가 동일하다

한 우상향 그래프를 기준으로
(1) 각 점에서 다 우하향 그래프 그려보기 (모든 경우의 수)
(2) 이번 우상향 그래프 내에서는 우하향 그래프 안그리겠다.


=> ***** r+c가 짝수인 곳과 r+c가 홀수인 곳은 서로 독립적이다! pruning 할 때 중요함
'''




import sys

n = int(sys.stdin.readline())
chess = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]


lst = [[] for _ in range(2*n-1)]            # 우상향 대각선 기준으로 우선 잡아줌 (0 ~ 2*n-1)
for i in range(n):
    for j in range(n):
        if chess[i][j]==1:
            lst[i+j].append((i,j))

visited = [False] * (2*n-1)         # 우하향 부분은 방문처리로 할 예정
cnt = 0
def dfs(depth, cnt):
    global ans
    # 가지 치기 : 남은 공간에 다 두어도 지금 max를 못이김
    if ans >= (cnt + (2*n  - depth)//2):
        return

    # 종료 조건
    if depth >= 2*n-1:
        ans = max(ans, cnt)
        return 
    
    # 백트래킹 탐색 시작
    for x, y in lst[depth]:         # 현 우상향 선 중 한 점에서 가능한 우하향 선 다 그어보기
        if not visited[x-y]:        # 아직 우하향 선 없는 부분 중에 우하향 선 긋기
            visited[x-y] = True
            dfs(depth + 2, cnt + 1) # 현 depth에서 모든 점에 대각선 놓아보기
            visited[x-y] = False
    dfs(depth+2, cnt)               # 이번에는 요 depth에서 대각선 안놓고 넘어가보기

ans = 0
dfs(0, 0)
ans1 = ans
ans = 0
dfs(1,0)
ans2 = ans
print(ans1 + ans2)