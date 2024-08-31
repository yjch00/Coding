import sys


n, m = list(map(int, sys.stdin.readline().split()))
nums = list(map(int, sys.stdin.readline().split()))

nums.sort()

def bt(depth):
    if depth == m:
        print(' '.join(map(str, box)))
        return
    
    for i in range(n):
        if nums[i] in box:
            continue
        if box:
            if nums[i] < box[-1]:
                continue
        box.append(nums[i])
        bt(depth + 1)
        box.pop()

box = []
bt(0)