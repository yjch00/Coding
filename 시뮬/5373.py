import sys

def changeside(matrix):
    matrix[0][0], matrix[0][1], matrix[0][2], matrix[1][2], matrix[2][2], matrix[2][1], matrix[2][0], matrix[1][0], matrix[0][0] = matrix[2][0], matrix[1][0], matrix[0][0], matrix[0][1], matrix[0][2], matrix[1][2], matrix[2][2], matrix[2][1], matrix[2][0]

    return matrix



def change_L(cube):
    for i in [0,1,2]:
        cube[0][i][0], cube[1][i][0], cube[5][i][0], cube[3][i][0] = cube[3][i][0], cube[0][i][0], cube[1][i][0], cube[5][i][0]
    cube[4] = changeside(cube[4])
    return cube
def change_R(cube):
    for i in range(3):
        cube[0][i][2], cube[1][i][2], cube[5][i][2], cube[3][i][2] = cube[1][i][2], cube[5][i][2], cube[3][i][2], cube[0][i][2]
    cube[2] = changeside(cube[2])
    return cube
def change_U(cube):
    for i in range(3):
        cube[1][0][i], cube[2][0][i], cube[3][2][2-i], cube[4][0][i] = cube[2][0][i], cube[3][2][2-i], cube[4][0][i], cube[1][0][i]
    cube[0] = changeside(cube[0])
    return cube
def change_D(cube):
    for i in range(3):
        cube[1][2][i], cube[2][2][i], cube[3][0][2-i], cube[4][2][i] = cube[4][2][i], cube[1][2][i], cube[2][2][i], cube[3][0][2-i]
    cube[5] = changeside(cube[5])
    return cube


def change_F(cube):
    for i in range(3):
        cube[0][2][i], cube[2][i][0], cube[5][0][2-i], cube[4][2-i][2] = cube[4][2-i][2], cube[0][2][i], cube[2][i][0], cube[5][0][2-i]
    cube[1] = changeside(cube[1])
    return cube
def change_B(cube):
    for i in range(3):
        cube[0][0][i], cube[2][i][2], cube[5][2][2-i], cube[4][2-i][0] = cube[2][i][2], cube[5][2][2-i],cube[4][2-i][0], cube[0][0][i],
    cube[3] = changeside(cube[3])
    return cube



n = int(sys.stdin.readline())
for _ in range(n):
    m = int(sys.stdin.readline())
    rotates = sys.stdin.readline().rstrip().split()
    cube = []
    for i in ['w', 'r', 'b', 'o', 'g', 'y']:
        cube.append([[i,i,i] for _ in range(3)])
    for r in rotates:
        if r[0] == 'L':     # 시계방향
            change_L(cube)
            if r[1] == '-':
                change_L(cube)
                change_L(cube)
        elif r[0] == 'R':
            change_R(cube)
            if r[1] == '-':
                change_R(cube)
                change_R(cube)
        elif r[0] == 'U':
            change_U(cube)
            if r[1] == '-':
                change_U(cube)
                change_U(cube)
        elif r[0] == 'D':
            change_D(cube)
            if r[1] == '-':
                change_D(cube)
                change_D(cube)
        elif r[0] == 'F':
            change_F(cube)
            if r[1] == '-':
                change_F(cube)
                change_F(cube)
        elif r[0] == 'B':
            change_B(cube)
            if r[1] == '-':
                change_B(cube)
                change_B(cube)
        # print(r)
    for i in range(3):
        print(*cube[0][i], sep='')       
            
            
         
            
            

