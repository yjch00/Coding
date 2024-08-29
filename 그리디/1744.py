# 1은 곱할때보다 더할때 좋다 
# 0은 음수 하나 지울때 용도. 음수 안남으면 그냥 더하기
# 나머지는 절대값 큰순서대로 정렬후 곱하기

import sys

n = int(sys.stdin.readline())
nums_p = []
nums_m = []
result = 0

for _ in range(n):
    tmp = int(sys.stdin.readline())
    if tmp > 1 :
        nums_p.append(tmp)
    elif tmp <= 0:
        nums_m.append(tmp)
    else:
        result += 1
nums_p.sort(reverse=True)
nums_m.sort()




for i in range(0,len(nums_p),2):
    if i+1 >= len(nums_p):
        result += nums_p[i]
    else:
        result += (nums_p[i]*nums_p[i+1])

for i in range(0, len(nums_m), 2):
    if i+1 >= len(nums_m):
        result += nums_m[i]
    else:
        result += (nums_m[i]*nums_m[i+1])

print(result)