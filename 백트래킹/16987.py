# *답지참고
'''
케이스가 세 개
(1) 깨진 계란을 쥔 경우 (넘어가기)
(2) 안깨진 계란을 쥐었는데 모두 깨져서 칠 게 없음
(3) 안깨진 계란을 쥐었고 이제 칠 거임


'''
import sys

n = int(sys.stdin.readline())
eggs = []
for _ in range(n):
    eggs.append(list(map(int, sys.stdin.readline().split())))


broken = 0
total = 0

def check(arr):
    cnt = 0
    for i in arr:
        if i[0] <= 0:
            cnt += 1
    return cnt


def bt(depth, arr):
    global total
    
    if depth > n-1:
        total = max(total, check(arr))
        return 
    
    # 이미 계란이 다 깨진경우 (손에 쥔건 상관없이)
    is_all_broken = True
    for i in range(n):
        if i == depth:
            continue
        if arr[i][0] > 0:
            is_all_broken = False
            break
    if is_all_broken:
        total = max(total, check(arr))
        return


    if arr[depth][0] < 0: # 깨진 계란은 쥘 수 없으니 넘어가기
        bt(depth+1, arr)
    else:
       
        for i in range(n):
            if (arr[i][0] > 0) and (depth != i): # 이미 깨진 애는 칠 수 없으므로
                arr[i][0] -= arr[depth][1]
                arr[depth][0] -= arr[i][1]
                bt(depth+1, arr)
                arr[i][0] += arr[depth][1]
                arr[depth][0] += arr[i][1]

                
            
bt(0, eggs)
print(total)