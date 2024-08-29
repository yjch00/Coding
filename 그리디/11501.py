import sys

n = int(sys.stdin.readline().strip())
for _ in range(n):
    m = int(sys.stdin.readline().strip())
    nums = list(map(int, sys.stdin.readline().strip().split()))
    total_revenue = 0
    max_num = 0
    # start_index = 0
    # while start_index < m:
    #     # print(start_index)
    #     max_num = max(nums[start_index:])
    #     max_index = nums[start_index:].index(max_num) + start_index
    #     if max_index == start_index:
    #         break
    #     for i in range(start_index, max_index):
    #         total_revenue += max_num - nums[i]
    #     start_index = max_index + 1
    #     # print(start_index)
    for i in range(m-1, -1, -1):       # 뒤에서 부터 접근하면 쉽다 !!!
        if nums[i] > max_num:
            max_num = nums[i]
        else:
            total_revenue += (max_num - nums[i])
        
    print(total_revenue)

        