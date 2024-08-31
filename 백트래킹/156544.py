


import sys


n, m = list(map(int, sys.stdin.readline().split()))
nums = list(map(int, sys.stdin.readline().split()))
visited = [False] * n
nums.sort()
total = []

def dfs():
    if len(box) == m:
        print(*box)
        return
    
    last = 0
    for i in range(n):

        if box:
            if box[-1] > nums[i]:
                continue

        if not visited[i] and last != nums[i]:
            box.append(nums[i])
            last = nums[i]
            visited[i] = True
            dfs()
            box.pop()
            visited[i] = False


box = []
dfs()