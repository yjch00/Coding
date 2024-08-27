# 원형큐만들기


# import sys
# from collections import deque
# n, k = map(int,sys.stdin.readline().strip().split())
# queue = deque(range(1,n+1,1))
# tmp = 0
# # 7, 3
# index = k
# i = 0
# outlist = []
# while queue:
#     for _ in range(k-1):
#         queue.append(queue.popleft())
#     outlist.append(str(queue.popleft()))



# print('<'+', '.join(outlist)+'>')


import sys

# 입력 받기
n, k = map(int, sys.stdin.readline().split())

# 요세푸스 순열 생성
idx = 0
queue = [i for i in range(1, n+1)]
res = []
while queue:
    idx += k - 1  # k-1번째 인덱스까지 건너뛰기
    if idx >= len(queue):  # 인덱스가 범위를 넘어갈 경우
        idx %= len(queue)  # 나머지 연산을 통해 인덱스 계산
    print(idx)
    print(queue)
    res.append(str(queue.pop(idx)))  # k번째 수 제거 후 결과 배열에 추가

# 결과 출력
print("<", ", ".join(res), ">", sep="")


# idx 
# 2 4 6 8 10 12 14 16
# lenqueue
# 7 6 5 4 3 2 1
# real_idx
# 2 4 1 3 2 0 0
