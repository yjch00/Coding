'''
*답지참고

연속된 오름차순 숫자를 제외하고는 무조건 한번씩 옮겨야된다!!! (가장 긴 연속 부분 수열 문제)
1 4 3 5 2 7 6

4 5 6 을 제외하고는 다 한번씩 옮겨야함
2만을 못 옮기고 2를 앞으로 꺼내려면 1도 꺼내야 하기 때문

'''



import sys


n = int(sys.stdin.readline())
m = list(map(int, sys.stdin.readline().split()))

idx = [-1] * (n + 1)


for i, v in enumerate(m):
    idx[v] = i                  # 각 숫자의 index를 구한다 (위치정보)
# print(idx)
max_count = 0
count = 1
for i in range(1,n):
    if idx[i] < idx[i+1]:
        count += 1
        if count > max_count:
            max_count = count
    else:                       # 깨진 순간
        # if count > max_count:         # 이렇게 되면 틀림 (가장 긴 수열이 맨 뒤에있을 경우 깨지질 않으니 업데이트 안됨)
        #     max_count = count
        count = 1
if n == 1:
    print(0)
else:
    print(n - max_count)
        