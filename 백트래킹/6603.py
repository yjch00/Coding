


import sys


def dfs(depth):
    if depth == 6:
        print(*box)
        return          # return 필수 !!
    last = 0
    for i in range(len(nums)):
        if nums[i] in box:
            continue
        if box:
            if box[-1] > nums[i]:
                continue 
        if  last != nums[i]:
            box.append(nums[i])

            last = nums[i]
            dfs(depth + 1)
            box.pop()

while True:

    nums = list(map(int, sys.stdin.readline().strip().split()))
    if len(nums) == 1:
        break
    n = nums[0]
    nums = nums[1:]
    visited = [False] * n

    
    box = []
    dfs(0)
    print()


