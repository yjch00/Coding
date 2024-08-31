


import sys


def dfs(depth):
    if depth == n:
        aeiou = box.count('a')+box.count('e')+box.count('i')+box.count('o')+box.count('u')
        if (aeiou >= 1) and (n-aeiou)>=2:
            print(''.join(box))
        return          # return 필수 !!

    for i in range(len(nums)):
        if nums[i] in box:
            continue
        if box:
            if box[-1] > nums[i]:
                continue 

        box.append(nums[i])
        dfs(depth + 1)
        box.pop()


n,m = list(map(int, sys.stdin.readline().strip().split()))
nums = sys.stdin.readline().strip().split()
nums.sort()
visited = [False] * len(nums)


box = []
dfs(0)


