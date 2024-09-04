import sys


'''
1 => 1
2 => 2
3 => 3
4 => 5
5 => 8 ()
6 => 6
1 2 3 4 5 6


'''


n = int(sys.stdin.readline())

m = int(sys.stdin.readline())
if n == 1:
    for i in range(m):
        tmp = int(sys.stdin.readline())
    print(1)
else:
    dp = [0] * (n+1)
    dp[1], dp[2] = 1, 2
    for i in range(3,n+1):
        dp[i] = dp[i-1] + dp[i-2]
    if m == 0:
        print(dp[n])
    else:
        last_num = 1
        cnt = []
        total = 1
        for i in range(m):
            tmp = int(sys.stdin.readline())
            if tmp - last_num >  1:
                cnt.append(tmp - last_num)
            last_num = tmp + 1
        
        if n-last_num+1 > 1:
            cnt.append(n-last_num+1)
        
        if cnt:
            total = dp[cnt[0]]
            if len(cnt) > 1:
                for i in cnt[1:]:
                    total *= dp[i]
        # print(cnt)
        print(total)
