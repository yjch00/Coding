'''
9
1

98
89
87
78
98
12
10

0이랑 9 일때만 특수하다
'''


n = int(input())
dp = [[0] * 10 for _ in range(n+1)]
dp[0] = [0,1,1,1,1,1,1,1,1,1]
# if n < 3:
#     print(dp[n])
#     exit()
for i in range(1,n+1):
    dp[i][0] = dp[i-1][1]
    dp[i][9] = dp[i-1][8]
    for k in range(1,9):
        dp[i][k] = dp[i-1][k-1]+dp[i-1][k+1]
    
print(sum(dp[n-1])%1000000000)