import numpy as np
import pygame
import sys
from math import floor

#Global variables
ROWS = 6
COLUMNS = 7
PLAYER1 = (255, 255, 0) #yellow
PLAYER2 = (255, 0, 0) #red

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

def draw_board(board):
    pygame.draw.rect(screen, (0,0,255), (0, SQUARESIZE, width, height-SQUARESIZE))
    for r in range(ROWS):
        for c in range(COLUMNS):
            if board[r][c] == 0:    
                pygame.draw.circle(screen, (0, 0, 0), (c*SQUARESIZE + SQUARESIZE//2, r*SQUARESIZE + SQUARESIZE + SQUARESIZE//2), RADIUS)
            elif board[r][c] == 1:
                pygame.draw.circle(screen, PLAYER1, (c*SQUARESIZE + SQUARESIZE//2, r*SQUARESIZE + SQUARESIZE + SQUARESIZE//2), RADIUS)
            elif board[r][c] == 2:
                pygame.draw.circle(screen, PLAYER2, (c*SQUARESIZE + SQUARESIZE//2, r*SQUARESIZE + SQUARESIZE + SQUARESIZE//2), RADIUS)
    pygame.display.update()

#game setup

board = create_board()
game_over = False
turn = 0


#pygame setup

pygame.init()

SQUARESIZE = 100
height = SQUARESIZE * (ROWS + 1) #one extra row to show the peice we are dropping
width = SQUARESIZE * COLUMNS 
size = (height, width)
RADIUS = SQUARESIZE//2 -6

screen = pygame.display.set_mode(size)
draw_board(board)
pygame.display.update()
myfont = pygame.font.SysFont('monospace', 75)

#main game loop
while not game_over:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        #scrolling coin
        if event.type == pygame.MOUSEMOTION:
            pygame.draw.rect(screen, (0,0,0), (0, 0, width, SQUARESIZE))
            x = event.pos[0]
            if turn == 0:
                pygame.draw.circle(screen, PLAYER1, (x, SQUARESIZE//2), RADIUS)
            elif turn == 1:
                pygame.draw.circle(screen, PLAYER2, (x, SQUARESIZE//2), RADIUS)
            pygame.display.update()

        if event.type == pygame.MOUSEBUTTONDOWN:
           
            if turn == 0:
                x = event.pos[0] #returns a tuple of coordinate of mouseclick
                choice = floor(x/SQUARESIZE)
                if is_valid(board, choice):
                    row = get_next_open_row(board, choice)
                    drop_piece(board, row, choice, 1)
                    
                    if winning_move(board, 1):
                        pygame.draw.rect(screen, (0,0,0), (0, 0, width, SQUARESIZE))
                        label = myfont.render('PLAYER 1 WINS!!!', 1, PLAYER1)
                        screen.blit(label, (30,10))
            
            else:
                x = event.pos[0] #returns a tuple of coordinate of mouseclick
                choice = floor(x/SQUARESIZE)
                if is_valid(board, choice):
                    row = get_next_open_row(board, choice)
                    drop_piece(board, row, choice, 2)
                    
                    if winning_move(board, 2):
                        pygame.draw.rect(screen, (0,0,0), (0, 0, width, SQUARESIZE))
                        label = myfont.render('PLAYER 2 WINS!', 1, PLAYER2)
                        screen.blit(label, (30,10))
                        game_over = True
                    

            draw_board(board)
                    
            turn += 1
            turn %= 2

            if game_over:
                pygame.time.wait(3000)
