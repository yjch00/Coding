# tmp = sys.stdin.readline().strip() 개행문자를 지우기 위해 꼭 string으로 쓸 거면 strip 붙여야됨
# for break else

# import sys


# n = int(sys.stdin.readline().strip())
# for _ in range(n):
#     stack = []
#     tmp = sys.stdin.readline().strip()
#     for j in tmp:
#         if j == '(':
#             stack.append(j)
#         else:
#             if not stack:
#                 print('NO')
#                 break
#             stack.pop()
#         # print(stack)
#     if not stack:        
#         print('YES')
#     else:
#         print('NO')


import sys

n = int(sys.stdin.readline().strip())  # 첫 번째 입력을 읽고 개행문자를 제거합니다
for _ in range(n):
    stack = []
    tmp = sys.stdin.readline().strip()  # 각 테스트 케이스를 읽고 개행문자를 제거합니다
    for char in tmp:
        if char == '(':
            stack.append(char)
        else:  # char == ')'
            if not stack:
                print('NO')
                break
            stack.pop()
    else:  # for문이 break 없이 종료되면 실행됩니다
        if not stack:  # 스택이 비어있으면 올바른 괄호 문자열입니다
            print('YES')
        else:
            print('NO')