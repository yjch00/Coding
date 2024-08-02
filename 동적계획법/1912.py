n = int(input())
nums = list(map(int, input().split()))

id = [0] * n
id[0] = nums[0] 
for i in range(1,n):
    id[i] = max(id[i-1]+nums[i], nums[i])
print(max(id))