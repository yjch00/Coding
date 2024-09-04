import sys

n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
if n == 1:
    print(nums[0])
else:
    dp = [0] * (n + 1)
    for i in range(1,n+1):
        dp[i] = nums[i-1]
    for i in range(2, n+1):
        for j in range(1,i):
            dp[i] = max(dp[j]+dp[i-j], dp[i])
    print(dp[-1])
    