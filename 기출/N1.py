'''
문자열 S와 이름 배열 L이 주어진다.
문자열 S의 문자들로 주어진 배열의 각 이름을 몇개나 만들 수 있을지 세어보고 최대 제작가능 횟수를 반환한다.
S=LILLYBILLYBOO, L=['BILL', 'MARIA', 'LILLY'] 일때 BILL은 2번, MARIA는 0번, LILLY는 1번 만들 수 있다. 따라서 2를 반환해야 한다.
'''

def solutionTask1(S, L):
    scnt = {}
    mx = 0
    for s in S: 
        if s not in scnt.keys():
            scnt[s]=1
        else:
            scnt[s]+=1
        # 현재 가지고 있는 key의 개수

    for name in L:
        ncnt = {}
        for c in name:
            if c not in ncnt.keys():
                ncnt[c] = 1
            else:
                ncnt[c] += 1
        # 각 이름에 필요한 알파벳 개수

        curret = 999
        for key in ncnt.keys():
            if key not in scnt.keys(): # 이름의 알파벳이 s의 알파벳에 없는 경우
                curret = 0
                break
            curret = min(curret, scnt[key] // ncnt[key]) # for문 돌면서 가지고 있는 개수 나누기 필요한 이름 알파벳 개수 (몇 개 만들 수 있는지)의 최소값
        mx = max(mx, curret)
    return mx
print('sol2')

print(solutionTask1('LILLYBILLYBOO', ['BILL', 'MARIA', 'LILLY']))
print('sol2')
'''
- 배열 A와 기준 R이 주어진다.
- 배열 A에서 R 길이만큼을 빼고 남은 값들의 종류의 개수가 최대가 되는 경우를 찾아, 그 종류의 개수를 반환하라
- 배열의 순서는 바꿀 수 없다. A의 길이는 최대 10만. 배열의 원소 값도 최대 10만이었던걸로 기억한다.
- A=[2, 3, 1, 4, 2, 2], R=3 일때 [4, 2, 2]를 빼면 남은 값의 종류의 개수가 3으로 최대가 된다.
'''

def solutionTask2(A, R):
    # 가장 종류 적은 부분 R을 찾는다
    minidx, minuniq = 0, 2e9
    for i in range(len(A)-R+1):
        if i == 0:
            tmp = A[R:]
        else:
            tmp = A[:i]+A[i+R:]
        # print(tmp)
        minidx = max(minidx,len(set(tmp)))
    return minidx
print(solutionTask2([2, 3, 1, 4, 2, 2],3))
print(solutionTask2([2, 3, 1, 1, 2],2))


print('sol3')
'''
N * M 의 지도 B가 주어진다. 지도의 각 셀은 # 혹은 . 로 표현된다.
지도에는 patrol, submarine, destroyers라는 세가지 타입의 배가 #로 표시되어있다.
'''
