import sys

n = int(sys.stdin.readline())

nums = []
for _ in range(n):
    nums.append(int(sys.stdin.readline()))


first = nums[-1]
score = 0
for i in range(-2, -len(nums)-1, -1):

    # if first >= i: # 수정해줘야함
    #     score += (first - i + 1) 
    #     first = first + 1
    # else:
    #     first = i
    if nums[i] >= first:
        score += (nums[i] - first + 1 )
        first = first - 1
    else:
        first = nums[i]
    # print(first)

print(score)

