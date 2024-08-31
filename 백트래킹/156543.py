'''
1 7 9 9 인경우
1 9, 1 9 이렇게 두번 나오는 케이스 막기위해 last 존재


9 9 는 되고 1 9, 1 9 두번 나오는 것은 막아야 함
index 0에서 index 1로 넘어갈때는 새로운 dfs로 접근
index 0이 1인지 7인지 9인지는 for 문에서 결정. = > 이때 9랑 9는 다시 등장하지 않도록 해야함 (last의 존재 의의)

'''


import sys


n, m = list(map(int, sys.stdin.readline().split()))
nums = list(map(int, sys.stdin.readline().split()))
visited = [False] * n
nums.sort()
total = []

def dfs():
    if len(box) == m:
        print(*box)
    
    last = 0
    for i in range(n):

            

        if not visited[i] and last != nums[i]:
            box.append(nums[i])
            last = nums[i]
            visited[i] = True
            dfs()
            box.pop()
            visited[i] = False


box = []
dfs()