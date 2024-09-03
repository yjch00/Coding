import sys


n = int(sys.stdin.readline())
dp = [0]*(n+1)
dp[1] = 0
path = ['' for _ in range(n+1)]
path[1] = '1'


for i in range(1, n):
    prev = i 
    dp[i+1] = dp[i] + 1
    if (i+1) % 3 == 0 and dp[(i+1)//3] + 1 < dp[i+1]:
        dp[i+1] = dp[(i+1)//3] + 1
        prev = (i+1)//3
    if (i+1) % 2 == 0 and dp[(i+1)//2] + 1 < dp[i+1]:
        dp[i+1] = dp[(i+1)//2] + 1
        prev = (i+1)//2
    path[i+1] = str(i+1)+' '+path[prev] 

print(dp[n])
print(path[n])


        