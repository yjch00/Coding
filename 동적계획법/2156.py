import sys

'''
2번 연속 마시기는 되는데 3번 연속은 안된다
i-2랑 i번째 마시기
i-3랑 i-1 번째 마시기

dp[i] = dp[i-2] + wines[i]                  (i-1 에서 쉬기) : i-2까지 어떻든 상관없음
dp[i] = dp[i-3] + wines[i-1] + wines[i]     (i-2 에서 쉬기) : i-3까지 어떻든 상관없음
dp[i] = dp[i-1]                             (i   에서 쉬기) : i-1까지 어떻든 상관없음

'''
n = int(sys.stdin.readline())
dp = [0] * n
wines = [int(sys.stdin.readline()) for _ in range(n)]
if n == 1:
    print(wines[0])
elif n==2:
    print(wines[0]+wines[1])
else:

    dp[0] = wines[0]
    dp[1] = wines[0] + wines[1]
    dp[2] = max(wines[2]+wines[1], wines[2]+wines[0], dp[1])

    for i in range(3,n):
        dp[i] = max(dp[i-2]+wines[i], dp[i-3]+wines[i-1]+wines[i], dp[i-1])

        
    print(dp[-1])