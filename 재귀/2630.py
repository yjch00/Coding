import sys

n = int(sys.stdin.readline())
matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]




cnt_p = 0 
cnt_m = 0


def same_check(matrix):
    tmp = matrix[0][0]
    for i in matrix:
        for j in i:
            if j != tmp:
                return False
    return True


def solution(matrix):
    global cnt_p, cnt_z, cnt_m
    # print(matrix)
    if len(matrix) == 1:
        if matrix[0][0] == 1:
            cnt_p += 1
        else:
            cnt_m += 1
        return
    if same_check(matrix):
        if matrix[0][0] == 1:
            cnt_p += 1
        else:
            cnt_m += 1
        return
    else:
        length = len(matrix)//2
        solution([i[:length] for i in matrix[:length]])
        solution([i[:length] for i in matrix[length:]])
        solution([i[length:] for i in matrix[:length]])
        solution([i[length:] for i in matrix[length:]])
        
        

solution(matrix)

print(cnt_m)
print(cnt_p)
