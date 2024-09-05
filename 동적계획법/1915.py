import sys

n,m = map(int, sys.stdin.readline().split())
maps = []
for i in range(n):
    tmp = sys.stdin.readline().strip()
    maps.append(list(map(int, list(tmp))))


dp = [[0]*m for _ in range(n)]
ans = 0

for i in range(n):
    for j in range(m):
        if i == 0 or j == 0:
            dp[i][j] = maps[i][j]
        elif maps[i][j] == 0:
            dp[i][j] = 0
        else:
            dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
        ans = max(dp[i][j], ans)

# print(dp)
print(ans**2)

'''
Idea !!

dp[i][j] = min(maps[i][j-1], maps[i-1][j], maps[i-1][j-1]) + 1
1

11
12

111
122
123

1111
1222
1233
1234


'''