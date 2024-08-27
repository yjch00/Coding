# for break else 구문
# stdin.readline은 '\n'이 아닌 '.'을 기준으로 문장이 주어질때는 적절치 않은듯?

# 여기 주석풀고 제출하면 출력 초과가 나온다
# import sys
# input = sys.stdin.readline



import sys

while True:
    # text = sys.stdin.readline()
    text = input()
    
    if text == '.':
        break
    text = text.split('.')[0]
    stack1 = []
    
    for i in text:
        if i == '(':
            stack1.append(i)
        elif i == '[':
            stack1.append(i)
        elif i == ')':
            if not stack1:
                print('no')
                break
            tmp = stack1.pop()
            if tmp != '(':
                print('no')
                break 
        elif i == ']':
            if not stack1:
                print('no')
                break
            tmp = stack1.pop()
            if tmp != '[':
                print('no')
                break 
    else:
        if not stack1:
            print('yes')
        else:
            print('no')
