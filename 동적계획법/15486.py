import sys



n = int(sys.stdin.readline())
nums = []

dp = [0] * (n+1)        # dp[1] 은 1일차가 끝나고 얻을 수 있는 임금  (if 1 1)
for i in range(0,n):
    Ti, Pi = map(int, sys.stdin.readline().split())
    dp[i+1] = max(dp[i+1], dp[i])
    if i+Ti < n+1:
        dp[i + Ti] = max(dp[i + Ti], dp[i] + Pi)    # dp[0+1] = max(dp[0+1], dp[0] + 1)
    print(i, Ti, Pi)
    print(dp)
print(dp[-1])