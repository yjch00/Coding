

n = int(input())

dp = [0] * (1000001)

dp[1] = 0
dp[2] = 1
dp[3] = 1
dp[4] = 2
if n < 5:           # n 이 5보다 작은 경우 꼭 달 것
    print(dp[n])
    exit()

for i in range(5, n+1):
    if i % 6 == 0:
        dp[i] = min(dp[i//3]+1, dp[i//2]+1, dp[i-1]+1)
    elif i % 3 == 0:
        dp[i] = min(dp[i//3]+1, dp[i-1]+1)
    elif i % 2 == 0:
        dp[i] = min(dp[i//2]+1, dp[i-1]+1)
    else:
        dp[i] = dp[i-1]+1
        
print(dp[n])

