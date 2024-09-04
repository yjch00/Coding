import sys

'''
T = 7, W = 2


2
1
1
2
2
1
1

가로 방향이 t

[[0, 0, 0], [0, 1, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
[[0, 0, 0], [0, 1, 0], [1, 1, 2], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
[[0, 0, 0], [0, 1, 0], [1, 1, 2], [2, 1, 3], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
[[0, 0, 0], [0, 1, 0], [1, 1, 2], [2, 1, 3], [2, 3, 3], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
[[0, 0, 0], [0, 1, 0], [1, 1, 2], [2, 1, 3], [2, 3, 3], [2, 4, 3], [0, 0, 0], [0, 0, 0]]
[[0, 0, 0], [0, 1, 0], [1, 1, 2], [2, 1, 3], [2, 3, 3], [2, 4, 3], [3, 4, 5], [0, 0, 0]]
[[0, 0, 0], [0, 1, 0], [1, 1, 2], [2, 1, 3], [2, 3, 3], [2, 4, 3], [3, 4, 5], [4, 4, 6]]
'''




T,W = map(int, sys.stdin.readline().split())
jadu = [0] + [int(sys.stdin.readline()) for _ in range(T)]
dp = [[0] * (W+1) for _ in range(T+1)]

if jadu[1] == 1:
    dp[1][0] , dp[1][1] = 1, 0
else:
    dp[1][0], dp[1][1] = 0, 1
# print(dp)
for t in range(2 , T+1):
    for w in range(W+1):
        j = 0
        if w % 2 == 0 and jadu[t] == 1: # 짝수번 자리를 바꾸고 사과가 1번에 떨어지는 경우
            j = 1
        if w % 2 == 1 and jadu[t] == 2: # 홀수번 자리를 바꾸고 사과가 2번에 떨어지는 경우
            j = 1
        dp[t][w] = max(dp[t-1][0:w+1]) + j   # w+1의 최댓값 : W+1 
print(max(dp[-1]))