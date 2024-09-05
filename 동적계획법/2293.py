import sys


n,k = map(int, sys.stdin.readline().split())
nums = [int(sys.stdin.readline()) for _ in range(n)]
nums.sort()
dp = [0] * (k+1)
dp[0] = 1


for i in nums:
    for j in range(i, k+1):
        dp[j] += dp[j-i]  
print(dp[k])




'''
3 10
1
2
5


(if i = 1) dp[1] = 1, dp[2] = 1,  
(if i = 2) dp[2] = 1+dp[2], dp[2] = 1,  

각 코인을 차근차근 dp에 더해주면서 
1코인을 1개 쓴 경우, 2개 쓴 경우, 3개 쓴경우, ...
2코인을 1개 쓴 경우, 2개 쓴 경우, ...
계속 앞에 값에 누적해서 더해준다. 왜냐하면 1코인 개수와 2코인 개수는 서로 독립이니까.

dp[0] = 1 을 넣음으로써 1코인 1개쓴 경우, 2코인 1개쓴 경우, 5코인 1개쓴 경우 채워줌.


'''