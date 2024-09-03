import sys


n = int(sys.stdin.readline().strip())
nums = []
for _ in range(n):
    nums.append(list(map(int, sys.stdin.readline().strip().split())))

if n == 1:
    print(nums[0][0])
    exit()

for i in range(n-2,-1, -1): # (3, -1, -1)
    for j in range(i+1):     # 4
        nums[i][j] = nums[i][j] + max(nums[i+1][j], nums[i+1][j+1])
print(nums[0][0])