


'''
dp[i] = dp[i-1] + 

마지막 자리수
0 => 10개
1 => 9개
2 => 8개
3 => 7개
4 => 6개
5 => 5개
6 => 4개
7 => 3개
8 => 2개
9 => 1개



!!! 모듈러 연산을 하면 좋다

(A + B) % C = ((A % C) + (B % C)) % C
'''

import sys
n = int(sys.stdin.readline())
dp = [[0] * 10 for _ in range(n)]
dp[0] = [1]*10
# print(dp)
for i in range(1, n):
    for j in range(10):
        for k in range(j+1):
            dp[i][j] += dp[i-1][k]
        dp[i][j] %= 10007
# print(dp)
print(sum(dp[-1])%10007)

# import sys
# n = int(sys.stdin.readline())
# dp = [1] * 10
# for i in range(1,n):
#     for j in range(1,10):
#         dp[j] += dp[j-1]%10007    
# print(sum(dp)%10007)

'''
dp[1] = dp[1] + dp[0]
dp[2] = dp[2] + dp[1] + dp[0]

~~

'''