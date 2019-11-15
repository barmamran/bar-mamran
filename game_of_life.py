from copy import copy, deepcopy
DEAD = 0
ALIVE = 1
initial_board = [
    [DEAD, DEAD, DEAD, DEAD, DEAD, DEAD, DEAD],
    [DEAD, DEAD, ALIVE, DEAD, ALIVE, DEAD, DEAD],
    [DEAD, DEAD, ALIVE, ALIVE, ALIVE, DEAD, DEAD],
    [DEAD, DEAD, DEAD, DEAD, DEAD, DEAD, DEAD],
    [DEAD, DEAD, DEAD, DEAD, DEAD, DEAD, DEAD],
]

def check_bounds(i, j, mat):
    n = len(mat)
    m = len(mat[0])
    return i >=0 and i < n and j>=0 and j < m

def check_cond(prev_board,next_board, row, col):
    die_cnt = 0
    live_cnt = 0
   
    for i in range(row - 1, row + 2):
        for j in range(col - 1, col + 2):
            if i == row and j == col:
                continue
            else:
                if  check_bounds(i, j, prev_board) and prev_board[i][j] == DEAD :
                    die_cnt = die_cnt + 1
                elif (check_bounds(i, j, prev_board) and prev_board[i][j] == ALIVE):
                    live_cnt = live_cnt + 1
    if prev_board[row][col] == ALIVE:
        if live_cnt < 2 or live_cnt > 3:
            next_board[row][col] = DEAD
    else:
        if live_cnt == 3:
            next_board[row][col] = ALIVE
    

def game_of_life(initial_board, steps):
    if initial_board == []:
        return []

    prev_board = initial_board
    #next_board[1][2]=0
    for step in range(steps):
        next_board = deepcopy(prev_board)
        for i in range(len(prev_board)):
            for j in range(len(prev_board[i])):
                check_cond(prev_board,next_board, i, j)
        prev_board = deepcopy(next_board)
    finish = next_board.copy()
    return finish
    
print(game_of_life(initial_board, 4))

