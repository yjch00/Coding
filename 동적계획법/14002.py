'''
증가하는 수열

'''


import sys

n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
dp = [1] * (n)
b = [[nums[i]] for i in range(n)]
if n == 1:
    print(1)
    print(nums[0])
else:
    dp[1] = 1
    b[1] = [nums[1]]
    for i in range(1, n):
       
        for j in range(i):
            if nums[j] < nums[i]:
                if dp[j]+1 > dp[i]:    
                    dp[i] = dp[j]+1
                    b[i] = b[j] + [nums[i]]
        # if dp[i-1] > dp[i]:
        #     dp[i] = dp[i-1]
        #     b[i] = b[i-1]
                
    # len_list = [len(i) for i in b]
    # print(max(len_list))
    # print(' '.join(map(str, b[len_list.index(max(len_list))])))    


    m = max(dp)
    print(m)
    print(*b[dp.index(m)])


