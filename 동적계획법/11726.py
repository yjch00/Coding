import sys


n = int(sys.stdin.readline())
dp = [0] * (n+1)
dp[1] = 1
if n == 1:
    print(1)
elif n==2:
    print(2)
else:
    dp[2] = 2

    for i in range(3,n+1):
        dp[i] = dp[i-1] + dp[i-2]
    print(dp[n]%10007)