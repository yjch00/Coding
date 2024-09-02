import sys


'''
A^B % C
(if B 짝수) ((A^(B//2)%C) * (A^(B//2)%C))%C
(if B 홀수) ((A^(B//2)%C) * (A^(B//2)%C) * (A%C))%C

'''


A, B, C = map(int, sys.stdin.readline().split())
def solution(A, B, C):
    if B == 1:                  # 가장 많이 쪼개졌을때
        return(A%C)

    tmp = solution(A, B//2, C)  # 여기서부터 재귀적으로 쪼개져서 들어감.


    if B % 2 == 1:
        return ((tmp*tmp)%C)*A%C       # 다시 합쳐지는 과정
    else:
        return (tmp * tmp) % C
print(solution(A, B,C))

