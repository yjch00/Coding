
def fac(num):
    if num < 2:
        return 1
    
    return num * fac(num - 1) # 오른쪽으로 계속 곱해나가고 싶을 때
a = int(input())
print(fac(a))