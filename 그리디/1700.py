# idea : 가장 나중에 출현하는 용품의 코드를 뽑자
# 집합 사용 (add랑 remove)


import sys


n,k = list(map(int, sys.stdin.readline().split()))
nums = list(map(int, sys.stdin.readline().split()))

consents = set([])
count = 0
for i in range(len(nums)):
    if (nums[i] not in consents) and (len(consents) < n):
        consents.add(nums[i])
    elif nums[i] in consents:
        pass
    else:
        
        max_index = -1
        for obj in consents:
            try:
                num_index = nums[i+1:].index(obj)
            except:
                num_index = k  # 나중에 출현하지 않는다면 가장 뽑아버려야됨
            if max_index < num_index:
                last_obj, max_index = obj, num_index
        consents.remove(last_obj)
        consents.add(nums[i])
        count += 1

print(count)


