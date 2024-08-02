n = int(input())
colors = [list(map(int, input().split()))for _ in range(n)]
maps = [[0,0,0] for _ in range(n)]
maps[0] = colors[0]
for i in range(1, n):
    maps[i][0] = min(maps[i-1][1], maps[i-1][2]) + colors[i][0]
    maps[i][1] = min(maps[i-1][0], maps[i-1][2]) + colors[i][1]
    maps[i][2] = min(maps[i-1][0], maps[i-1][1]) + colors[i][2]
print(min(maps[-1]))
    