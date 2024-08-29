import sys

total = sys.stdin.readline().strip()
total = total.split('-')

sumall = list(map(int, total[0].split('+')))
sumall = sum(sumall)
if len(total) == 1:
    print(sumall)
else:
    for i in total[1:]:
        tmp = list(map(int, i.split('+')))
        tmp = sum(tmp)
        sumall -= tmp
    print(sumall)