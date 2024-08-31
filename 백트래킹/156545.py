


import sys


n, m = list(map(int, sys.stdin.readline().split()))
nums = list(map(int, sys.stdin.readline().split()))
nums = list(set(nums))

nums.sort()
total = []

def dfs(depth):
    if depth == m:
        print(*box)
        return          # return 필수 !!
    for i in range(len(nums)): 
        box.append(nums[i])
        dfs(depth + 1)
        box.pop()



box = []
dfs(0)