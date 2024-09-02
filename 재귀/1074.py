import sys

n, r, c = map(int, sys.stdin.readline().split())



cnt = 0
def solution(n, r, c):
    if n == 1:
        if r == 0 and c == 0:
            return 0
        elif r == 0 and c == 1:
            return 1
        elif r == 1 and c == 0:
            return 2
        elif r == 1 and c == 1:
            return 3
    
    cnt = solution(n-1, r%(2**(n-1)), c%(2**(n-1)))
    if r < 2**(n-1) and c < 2**(n-1):  # 1사분면
        return (cnt + 0)
    elif r < 2**(n-1) and c >= 2**(n-1): # 2사분면
        return(cnt + (2**(n-1))**2)
    elif r >= 2**(n-1) and c < 2**(n-1): # 3사분면
        return(cnt + (2**(n-1))**2 * 2)
    elif r >= 2**(n-1) and c >= 2**(n-1):
        return(cnt + (2**(n-1))**2 * 3)


print(solution(n, r, c))