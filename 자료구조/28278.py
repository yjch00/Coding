# 스택은 그냥 list로 푼다
# 1자리 숫자여도 list 형태로 받으려면(string) sys.stdin.readline().split()
import sys


input=sys.stdin.readline
stack = []
n=int(input())
for _ in range(n):
    nums = sys.stdin.readline().split()
    if nums[0]=='1':
        stack.append(nums[1])
    elif nums[0]=='2':
        if len(stack)==0:
            print(-1)
        else:
            print(stack.pop())
    elif nums[0]=='3':
        print(len(stack))
    elif nums[0]=='4':
        if len(stack)==0:
            print(1)
        else:
            print(0)
    else:
        if len(stack)==0:
            print(-1)
        else:
            print(stack[-1])
    