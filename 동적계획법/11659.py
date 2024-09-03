import sys


n, m = map(int, sys.stdin.readline().strip().split())
nums = list(map(int, sys.stdin.readline().strip().split()))


sum_list = [0] * (n+1)
sum_list[0] = 0

for i in range(1,n+1):
    sum_list[i] = sum_list[i-1] + nums[i-1]

# print(sum_list)

for _ in range(m):
    a, b = map(int, sys.stdin.readline().strip().split())
    print(sum_list[b] - sum_list[a-1])

