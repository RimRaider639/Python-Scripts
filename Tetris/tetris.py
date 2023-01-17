import pygame
import random

# creating the data structure for pieces
# setting up global vars
# functions
# - create_grid
# - draw_grid
# - draw_window
# - rotating shape in main
# - setting up the main

"""
10 x 20 square grid
shapes: S, Z, I, O, J, L, T
represented in order by 0 - 6
"""

pygame.font.init()

# GLOBALS VARS
s_width = 800
s_height = 700
play_width = 300  # meaning 300 // 10 = 30 width per block
play_height = 600  # meaning 600 // 20 = 20 height per block
block_size = 30
ROWS = play_height // block_size
COLUMNS = play_width // block_size

top_left_x = (s_width - play_width) // 2
top_left_y = (s_height - play_height) // 2 + 10


# SHAPE FORMATS

S = [['.....',
      '......',
      '..00..',
      '.00...',
      '.....'],
     ['.....',
      '..0..',
      '..00.',
      '...0.',
      '.....']]

Z = [['.....',
      '.....',
      '.00..',
      '..00.',
      '.....'],
     ['.....',
      '..0..',
      '.00..',
      '.0...',
      '.....']]

I = [['..0..',
      '..0..',
      '..0..',
      '..0..',
      '.....'],
     ['.....',
      '0000.',
      '.....',
      '.....',
      '.....']]

O = [['.....',
      '.....',
      '.00..',
      '.00..',
      '.....']]

J = [['.....',
      '.0...',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..00.',
      '..0..',
      '..0..',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '...0.',
      '.....'],
     ['.....',
      '..0..',
      '..0..',
      '.00..',
      '.....']]

L = [['.....',
      '...0.',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..0..',
      '..0..',
      '..00.',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '.0...',
      '.....'],
     ['.....',
      '.00..',
      '..0..',
      '..0..',
      '.....']]

T = [['.....',
      '..0..',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..0..',
      '..00.',
      '..0..',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '..0..',
      '.....'],
     ['.....',
      '..0..',
      '.00..',
      '..0..',
      '.....']]

shapes = [S, Z, I, O, J, L, T]
shape_colors = [(0, 255, 0), (255, 0, 0), (0, 255, 255), (255, 255, 0), (255, 165, 0), (0, 0, 255), (128, 0, 128)]
# index 0 - 6 represent shape


class Piece(object):
	
    def __init__(self, col, row, shape):
        self.x = col
        self.y = row
        self.shape = shape
        self.color = shape_colors[shapes.index(shape)]
        self.rotation = 0

def create_grid(locked_positions={}): #locked_positions is a dict with (i,j) = (r, g, b)

    grid = [[(0,0,0) for x in range(COLUMNS)] for x in range(ROWS)]

    for i in range(ROWS):
        for j in range(COLUMNS):
            if (j,i) in locked_positions:
                color = locked_positions[(j,i)]
                grid[i][j] = color

    return grid


def convert_shape_format(shape):
    positions = []
    format = shape.shape[shape.rotation % len(shape.shape)] #shape.shape is a list (T is a list of lists of different orientations of T)

    for i, line in enumerate(format):
        for j, cell in enumerate(line):
            if cell == '0':
                positions.append((shape.x + j -2 , shape.y + i -4 )) #some offset to counter the effect of periods

    return positions

def valid_space(shape, grid):
    accepted_pos = [(j,i) for i in range(ROWS) for j in range(COLUMNS) if grid[i][j] == (0,0,0)]
    formatted = convert_shape_format(shape)
    for pos in formatted:
        if pos not in accepted_pos:
            if pos[1] > -1: #makes it valid even when the shapes are initially in negative rows (above top_most_y)
                return False 

    return True

def check_lost(positions):
    for x,y in positions:
        if y < 1: #checks if any shape is touching the topmost line (lost condition)
            return True
    return False

def get_shape():
	return Piece(5, 0, random.choice(shapes))


def draw_text_middle(text, size, color, surface):
    pass

    
   
def draw_grid(surface):
    for i in range(ROWS):
        pygame.draw.line(surface, (128,128,128), (top_left_x, top_left_y + i*block_size), (top_left_x + play_width, top_left_y + i*block_size))

    for j in range(COLUMNS):
        pygame.draw.line(surface, (128,128,128), (top_left_x + j*block_size, top_left_y), (top_left_x + j*block_size, top_left_y + play_height))

def clear_rows(grid, locked):
    pass


def draw_next_shape(shape, surface):
    font = pygame.font.SysFont('comicsans', 30)
    label = font.render('Next Shape:', 1, (255, 255, 255)) #Anti aliasing = 1

    x = top_left_x + play_width + 75
    y = top_left_y + play_height//2 - 100
    box_size = 20

    surface.blit(label, (x - 25 , y - 20))

    for i, line in enumerate(shape.shape[0]):
        for j, col in enumerate(line):
            if col == '0':
                pygame.draw.rect(surface, shape.color, (x + j*box_size, y + i*box_size, box_size, box_size))

def draw_window(surface, grid):
    surface.fill((0,0,0))
    #Tetris title
    pygame.font.init()
    font = pygame.font.SysFont('comicsans', 45)
    label = font.render('Tetris', 1, (255, 255, 255))
    surface.blit(label, (top_left_x + play_width//2 - label.get_width()/2, 2))

    for i in range(ROWS):
        for j in range(COLUMNS):
            pygame.draw.rect(surface, grid[i][j], (top_left_x + j*block_size, top_left_y + i*block_size, block_size, block_size), 0) #0 fills in the shape rather than drawing a border for it
    
    draw_grid(surface)
    pygame.draw.rect(surface, (255,0,0), (top_left_x-2, top_left_y, play_width+4, play_height+4), 5) #border of width 4

    # pygame.display.update()

def main(surface):
	
    locked_positions = {}
    grid = create_grid(locked_positions)
    run = True
    change_piece = False
    current_shape = get_shape()
    next_shape = get_shape()
    clock = pygame.time.Clock()
    fall_time = 0
    fall_speed = 0.27 #time until the next piece falls

    while run:
        grid = create_grid(locked_positions) #because locked position gets updated everytime
        fall_time += clock.get_rawtime()
        clock.tick()

        #controlling the falling of pieces
        if fall_time/1000 > fall_speed:
            fall_time = 0
            current_shape.y += 1
           
            if not(valid_space(current_shape, grid)) and current_shape.y > 0:
                current_shape.y -= 1
                change_piece = True

        
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.display.quit()
                quit()

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_UP:
                    current_shape.rotation += 1
                    if not valid_space(current_shape, grid):
                        current_shape.rotation -= 1

                elif event.key == pygame.K_DOWN:
                    current_shape.y += 1
                    if not valid_space(current_shape, grid):
                        current_shape.y -= 1

                elif event.key == pygame.K_RIGHT:
                    current_shape.x += 1
                    if not valid_space(current_shape, grid):
                        current_shape.x -= 1

                elif event.key == pygame.K_LEFT:
                    current_shape.x -= 1
                    if not valid_space(current_shape, grid):
                        current_shape.x += 1

        shape_pos = convert_shape_format(current_shape)
        # print(shape_pos)
        
        for i in range(len(shape_pos)):
            col, row = shape_pos[i]
            if row > -1:
                grid[row][col] = current_shape.color

        if change_piece:
            for pos in shape_pos:
                
                locked_positions[pos]= current_shape.color
            current_shape = next_shape
            next_shape = get_shape()
            change_piece = False

        
        draw_window(surface, grid)
        draw_next_shape(next_shape, surface)
        pygame.display.update()

        if check_lost(locked_positions):
            run = False

    

def main_menu():
	main(wn)

wn = pygame.display.set_mode((s_width, s_height))
pygame.display.set_caption('Tetris')
main_menu()  # start game