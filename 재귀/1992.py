'''
[list(sys.stdin.readline().strip()) for _ in range(n)]
[list(sys.stdin.readline().strip().split()) for _ in range(n)]

위에껀 잘 split이 되는데 오히려 아래꺼가 list 형태로 저장이 안됨...(왜지)

'''
import sys

n = int(sys.stdin.readline())

matrix = [list(sys.stdin.readline().strip()) for _ in range(n)]

coding = ''


def same_check(matrix):
    tmp = matrix[0][0]
    for i in matrix:
        for j in i:
            if j != tmp:
                return False
    return True


def solution(matrix):
    global coding

    if len(matrix) == 1:
        if matrix[0][0] == '1':
            coding += '1'
        else:
            coding += '0'
        return
    if same_check(matrix):
        if matrix[0][0] == '1':
            coding += '1'
        else:
            coding += '0'
        return
    else:
        length = len(matrix)//2
        coding += '('
        solution([i[:length] for i in matrix[:length]])
        solution([i[length:] for i in matrix[:length]])
        solution([i[:length] for i in matrix[length:]])
        solution([i[length:] for i in matrix[length:]])
        coding += ')'
        

solution(matrix)
print(coding)
