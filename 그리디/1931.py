import sys

n = int(sys.stdin.readline())
total = []


for _ in range(n):
    total.append(list(map(int, sys.stdin.readline().split())))

total.sort(key = lambda x:(x[1], x[0]))  # 중요!!!!!!!!!! sorting 방법


finish = total[0][1]
num = 1
for i in total[1:]:
    if i[0] >= finish:
        finish = i[1]
        num += 1
print(num)