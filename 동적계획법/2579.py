n = int(input())
nums = []
for _ in range(n):
    nums.append(int(input()))

id = [0] * 300
id[0] = nums[0] 

if n == 1:
    print(id[n-1])
    exit()

id[1] = nums[0]+nums[1]

if n == 2:
    print(id[n-1])
    exit()


id[2] = max(nums[0]+nums[2], nums[1]+nums[2])


for i in range(3,n):
    id[i] = max(id[i-3]+nums[i-1], id[i-2]) + nums[i]
print(id[n-1])