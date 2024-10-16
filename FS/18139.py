import sys
from collections import deque
maps = [list(map(int, sys.stdin.readline().split())) for _ in range(6)]

# 왼쪽 끝, 위 끝을 point로 설정
# 가로방향 : 0, 세로방향 : 1 // car : 0, truck : 1
vehicles_info = dict()
initial_state_dict = dict()

for i in range(6):
    for j in range(6):
        now = maps[i][j]
        if now == 0:
            continue
        if now not in vehicles_info:
            if j < 4 and maps[i][j+2] == now:
                vehicles_info[now] = (0, 1)
                initial_state_dict[now] = [i,j]
            elif j < 4 and maps[i][j+1] == now:
                vehicles_info[now] = (0, 0)
                initial_state_dict[now] = [i,j]
            elif j ==4 and maps[i][j+1] == now:
                vehicles_info[now] = (0, 0)
                initial_state_dict[now] = [i,j]
            elif i < 4 and maps[i+2][j] == now:
                vehicles_info[now] = (1, 1)
                initial_state_dict[now] = [i,j]
            elif i < 4 and maps[i+1][j] == now:
                vehicles_info[now] = (1, 0)
                initial_state_dict[now] = [i,j]
            elif i == 4 and maps[i+1][j] == now:
                vehicles_info[now] = (1, 0)
                initial_state_dict[now] = [i,j]
initial_state = []
max_id = max(vehicles_info.keys())
for i in range(1, max_id+1):
    initial_state.append(tuple(initial_state_dict[i]))
    
 
def create_map(state):
    new_maps = [[0]*6 for _ in range(6)]
    for idx, pos in enumerate(state):
        id = idx + 1
        x,y = pos
        a,b = vehicles_info[id]
        if a==0:
            for j in range(y, y+2+b):
                new_maps[x][j] = id
        else:
            for i in range(x, x+2+b):
                new_maps[i][y] = id
    return new_maps
            
            
        
    
def possible_move(state):
    moves = []
    new_maps = create_map(state)
    for idx, pos in enumerate(state):
        id = idx+1
        x,y = pos
        a,b = vehicles_info[id]
            # 왼쪽으로
        if a == 0: 
            if y > 0 and new_maps[x][y-1] == 0:
                new_state = list(state)
                new_state[idx] = (x, y-1)
                moves.append(tuple(new_state))
            # 오른쪽으로
            if b == 0:
                if y < 4 and new_maps[x][y+2] == 0:
                    new_state = list(state)
                    new_state[idx] = (x,y+1)
                    moves.append(tuple(new_state))
            else:
                if y<3 and new_maps[x][y+3] == 0:
                    new_state = list(state)
                    new_state[idx] = (x,y+1)
                    moves.append(tuple(new_state))
        else:
            # 위로
            if x>0 and new_maps[x-1][y] == 0:
                new_state = list(state)
                new_state[idx] = (x-1, y)
                moves.append(tuple(new_state))
            # 아래로
            if b == 0:
                if x < 4 and new_maps[x+2][y] == 0:
                    new_state = list(state)
                    new_state[idx] = (x+1,y)
                    moves.append(tuple(new_state))
            else:
                if x < 3 and new_maps[x+3][y] == 0:
                    new_state = list(state)
                    new_state[idx] = (x+1,y)
                    moves.append(tuple(new_state))
    return tuple(moves)
def is_goal(state):
    if state[0] == (2, 4):
        return True
    return False               


def dfs(state, depth):
    visited[state] = depth
    
    
    if depth > 8:
        return -1
    if is_goal(state):
        return depth
    moves = possible_move(state)
    for move in moves:
        if move not in visited or visited[move] > depth + 1:
            result = dfs(move, depth+1)
            if result != -1:
                ans.append(result)
    return -1
             
                 

ans = []
visited = dict()
initial_state = tuple(initial_state)
dfs(initial_state, 0)
print(min(ans)+2) if ans else print(-1)