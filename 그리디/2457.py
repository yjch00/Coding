
# 굳이 mon2day 안해도 되고 (1, 2) < (1, 3) < (2, 1)로 대교비소가능
import sys

def mon2day(a, b):
    
    day = 0
    for i in range(1,a):
        if i in [4, 6, 9, 11]:
            day += 30
        elif i in [1, 3, 5, 7, 8, 10, 12]:
            day += 31
        else:
            day += 28
    day += b
    return day
# print(mon2day(3,1), mon2day(11,30))   60, 334
n = int(sys.stdin.readline())
m = []
for _ in range(n):
    a, b, c, d = list(map(int, sys.stdin.readline().split()))
    m.append([mon2day(a,b), mon2day(c,d)])
m.sort(key=lambda x:(x[0], x[1]))   # m.sort() 랑 똑같다 !!!

first = 60
result = 0 
i = 0


while i<n:
    if (m[i][0] <= first) and (first < m[i][1]):
        max_end = m[i][1]
        while i < n-1: # 최고의 max end 찾기
            if first < m[i+1][0]: # i+1 이상부터 지금 while문과 관련이 없는 것 같으면 끝내버리기
                break
            if max_end < m[i+1][1]: # max_end 더 높은 값으로 변경
                max_end = m[i+1][1]
            i += 1
        result += 1
        first = max_end

        if first > 334:
            print(result)
            exit()
    i += 1
print(0)

