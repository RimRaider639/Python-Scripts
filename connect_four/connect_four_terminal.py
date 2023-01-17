import numpy as np

#Global variables
ROWS = 6
COLUMNS = 7

def create_board():
    board = np.zeros((ROWS, COLUMNS)) #6 rows, 7 columns
    return board

def drop_piece(board, row, column, piece):
    board[row][column] = piece

def is_valid(board, choice):
    return board[0][choice] == 0

def get_next_open_row(board, col):
    whole_col = [i[col] for i in board]
    whole_col.reverse()
    return ROWS -1 - whole_col.index(0)

def winning_move(board, piece):
    #checking rows
    for r in range(ROWS):
        for c in range(COLUMNS - 3): #no starting points in the last 3 columns (we need 4 consecutives)
            if board[r][c] == board[r][c+1] == board[r][c+2] == board[r][c+3] == piece:
                return True

    #checking columns
    for c in range(COLUMNS):
        for r in range(ROWS - 3):
            if board[r][c] == board[r+1][c] == board[r+2][c] == board[r+3][c] == piece:
                return True

    #checking positively sloped diagonals
    for c in range(COLUMNS - 3):
        for r in range(3, ROWS):
            if board[r][c] == board[r-1][c+1] == board[r-2][c+2] == board[r-3][c+3] == piece:
                return True


    #checking negatively sloped diagonals
    for c in range(COLUMNS - 3):
        for r in range(ROWS - 3):
            if board[r][c] == board[r+1][c+1] == board[r+2][c+2] == board[r+3][c+3] == piece:
                return True

board = create_board()
game_over = False
turn = 0
print(board)

while not game_over:

    #Ask player 1
    if turn == 0:
        choice = int(input('Player 1, select your column (0-6): '))
        if is_valid(board, choice):
            row = get_next_open_row(board, choice)
            drop_piece(board, row, choice, 1)
            print(board)
            
            if winning_move(board, 1):
                print('PLAYER 1 WINS!')
                game_over = True
        

    #Ask player 2
    else:
        choice = int(input('Player 2, select your column (0-6): '))
        if is_valid(board, choice):
            row = get_next_open_row(board, choice)
            drop_piece(board, row, choice, 2)
            print(board)
            
            if winning_move(board, 2):
                print('PLAYER 2 WINS!')
                game_over = True
            

    
            
    turn += 1
    turn %= 2
