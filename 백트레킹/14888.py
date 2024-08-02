

# 백트래킹
num = int(input())
num_list = list(map(int, input().split()))
cal_list = list(map(int, input().split()))

mx = -1e9
mn = 1e9


def dfs(n, tmp):
    global mx, mn
    
    if n == num - 1:
        mx = max(tmp, mx)
        mn = min(tmp, mn)
        return 
    
    if cal_list[0] != 0:
        cal_list[0] -= 1
        dfs(n+1, tmp+num_list[n+1])
        cal_list[0] += 1                # 시작을 + ([0])으로 안하는 애들이 있을 수 있으니 다시 복구해서 뒤로 넘겨줌
    
    if cal_list[1] != 0:
        cal_list[1] -= 1
        dfs(n+1, (tmp-num_list[n+1]))
        cal_list[1] += 1
    
    if cal_list[2] != 0:
        cal_list[2] -= 1
        dfs(n+1, (tmp*num_list[n+1]))
        cal_list[2] += 1
    
    if cal_list[3] != 0:
        cal_list[3] -= 1
        dfs(n+1, int(tmp/num_list[n+1]))
        cal_list[3] += 1
        
dfs(0, num_list[0])
print(mx, mn)