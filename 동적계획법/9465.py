import sys


'''
target [n][0] 이전에 가능한 케이스
Case1) [n-1][1]
Case2) [n-2][1]


*주의
[n-2][0] 인경우는 무조건 [n-1][1] 도 더한게 더 크기 때문에 무효!

target [n][1] 도 거꾸로 똑같다 !!

'''




t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    num1 = list(map(int, sys.stdin.readline().split()))
    num2 = list(map(int, sys.stdin.readline().split()))
    if n == 1:
        print(max(num1[0], num2[0]))
    elif n == 2:
        print(max(num1[0]+num2[1], num1[1]+num2[0]))
    else:
        dp = [[0,0] for _ in range(n)]
        dp[0] = [num1[0], num2[0]]
        dp[1] = [num1[1]+num2[0], num1[0]+num2[1]]
        for i in range(2,n):
            dp[i][0] = max(dp[i-1][1], dp[i-2][1]) +num1[i]
            dp[i][1] = max(dp[i-1][0], dp[i-2][0]) +num2[i]
        print(max(dp[-1][0], dp[-1][1]))
             
    
    