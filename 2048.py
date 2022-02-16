# https://open.kattis.com/problems/2048
# 0, 1, 2, 3
# left, up, right, down

no_of_lines = 5
board = []
move = 0

board = [list(map(int, input().split())) for _ in range(4)]

for i in range(no_of_lines):
    board.append(list(map(int, input().split())))
move = board[4][0]
del board[4]

if (move == 0):
    for row in board:
        for i in range(3,-1,-1):
            case = neighbor_check(row[i], row[i+1])
            if (case == 1):
                row[i+1] = i*2
                row[i] = 0
                break
            if (case == 2):
                if (neighbor_check(row[i], row[i+2]) == 
            
            
'''
returns
    1: match     
    2: 0
    3: no match
'''       
def neighbor_check(a, b):
    if a == b:
        return 1
    elif b == 0:
        return 2
    else:
        return 3
         
'''
if (move == 1):

if (move == 2):

if (move == 3):
'''
