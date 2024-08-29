import sys

m = sys.stdin.readline().strip()
word = m[0]
# print(type(word))


for i in range(1,len(m)):
    if m[i-1] == m[i]:
        pass
    else:
        word += m[i]

zero = word.count('0')

print(min(zero, len(word)-zero))