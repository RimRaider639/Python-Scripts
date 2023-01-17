import pygame as pg
from random import randrange
import tkinter as tk
from tkinter import messagebox

class Cube(object):

    rows, w = 20, 500

    def __init__(self, start, dirx = 1, diry = 0, color = (255, 0, 0)):
        self.pos = start
        self.dirx = 1
        self.diry = 0
        self.color = color
    
    def move(self, dirx, diry):
        self.dirx = dirx
        self.diry = diry
        self.pos= (self.pos[0] + self.dirx, self.pos[1] + self.diry)

    def draw(self, surface, eyes = False):
        box_dis = self.w // self.rows
        r = self.pos[0]
        c = self.pos[1]

        pg.draw.rect(surface, self.color, (r*box_dis+1, c*box_dis+1, box_dis-2, box_dis-2)) # (x, y, w, h) subtracting two because else it'll overlap the grid lines

        if eyes:
            center = box_dis // 2
            radius = 3
            
            eye1 = (r*box_dis + center - radius*2, c*box_dis + 8)
            eye2 = (r*box_dis + box_dis - radius*2, c*box_dis + 8) 

            pg.draw.circle(surface, (0,0,0), eye1, radius)
            pg.draw.circle(surface, (0,0,0), eye2, radius)


class Snake(object):

    body = []
    turns = {}

    def __init__(self, color, position): #the position here is (r,c) and not (x,y)
        self.color = color
        self.head = Cube(position)
        self.body.append(self.head)
        self.dirx = 0 # can be -1, 0, 1. when this is 1/-1, diry has to be zero and vice versa since snake can move in only one dir
        self.diry = 1
    
    def move(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.QUIT()

            keys = pg.key.get_pressed() #gives a dict of all keys with bool value describing pressed or not

            for key in keys:
                if keys[pg.K_LEFT]:
                    self.dirx = -1
                    self.diry = 0
                    self.turns[self.head.pos[:]] = [self.dirx, self.diry] # [:] makes a copy without changing the original variable

                elif keys[pg.K_RIGHT]:
                    self.dirx = 1
                    self.diry = 0
                    self.turns[self.head.pos[:]] = [self.dirx, self.diry]

                elif keys[pg.K_UP]:
                    self.dirx = 0
                    self.diry = -1
                    self.turns[self.head.pos[:]] = [self.dirx, self.diry]

                elif keys[pg.K_DOWN]:
                    self.dirx = 0
                    self.diry = 1
                    self.turns[self.head.pos[:]] = [self.dirx, self.diry]

        for i, cell in enumerate(self.body): #enumerate returns a counting value along withe the iterables
            p = cell.pos[:]
            if p in self.turns:
                turn = self.turns[p] #stores the position value of p
                cell.move(turn[0], turn[1])

                if i == len(self.body) - 1:
                    self.turns.pop(p)
            else:
                if cell.dirx == -1 and cell.pos[0] <= 0: cell.pos = (cell.rows - 1, cell.pos[1])
                elif cell.dirx == 1 and cell.pos[0] >= cell.rows - 1: cell.pos = (0, cell.pos[1])
                elif cell.diry == 1 and cell.pos[1] >= cell.rows - 1: cell.pos = (cell.pos[0], 0)
                elif cell.diry == -1 and cell.pos[1] <= 0: cell.pos = (cell.pos[0], cell.rows - 1)
                else: cell.move(cell.dirx, cell.diry)

    def addCube(self):
        
        tail = self.body[-1]
        dx, dy = tail.dirx, tail.diry

        if (dx, dy) == (1, 0):
            x, y = tail.pos[0]-1, tail.pos[1]
        elif (dx, dy) == (-1, 0):
            x, y = tail.pos[0]+1, tail.pos[1]
        elif (dx, dy) == (0, 1):
            x, y = tail.pos[0], tail.pos[1]-1
        elif (dx, dy) == (0, -1):
            x, y = tail.pos[0], tail.pos[1]+1

        self.body.append(Cube((x,y)))
        self.body[-1].dirx = dx
        self.body[-1].diry = dy

    def draw(self, surface):
        for i, cell in enumerate(self.body):
            if i == 0:
                cell.draw(surface, True) #draws eyes on the head
            else:
                cell.draw(surface)

    def reset(self, pos):
        self.head = Cube(pos)
        self.body = []
        self.body.append(self.head)
        self.turns = {}
        dirx, diry = 1,0


def drawGrid(w, rows, surface):
    grid_box_width = w // rows

    x = 0
    y = 0

    for i in range(rows):
        x += grid_box_width
        y += grid_box_width

        pg.draw.line(surface, (255, 255, 255), (x, 0), (x, w)) #vertical grid lines
        pg.draw.line(surface, (255, 255, 255), (0, y), (w, y)) #horizontal grid lines

def randomsnack(snake):
    global rows

    forbidden_pos = snake.body
    
    while 1:
        x, y = randrange(rows), randrange(rows) #randrange does the same thing as randint(range(rows))
        if len(list(filter(lambda z: z.pos == (x, y), forbidden_pos)))>0:
            continue
        else:
            break

    return(x,y)


def redrawWindow(surface):
    global width, rows, s, snack
    
    surface.fill((0,0,0)) #filling the window with black
    s.draw(surface)
    snack.draw(surface)
    drawGrid(width, rows, surface)
    pg.display.update()

def message_box(subject, content):
    root = tk.Tk()
    root.attributes("-topmost", True) #displays the window on top of everything else
    root.withdraw() #makes the window invisible (or forgotten, needs to be redrawn everytime)
    messagebox.showinfo(subject, content)

    try:
        root.destroy()
    except:
        pass

def main():
    global width, rows, s, snack
    highscore = 0
    width = 500
    rows = 20 #set to something that divides the height evenly
    wn = pg.display.set_mode((width, width)) #we are drawing a square surface
    s = Snake((255, 0, 0), (10,10))
    snack = Cube(randomsnack(s), color = (0, 255, 0))
    clock = pg.time.Clock()

    game_on = True
    while game_on:
        pg.time.delay(50) #x ms delay. The more this is, the slower it runs
        clock.tick(10) #makes sure the game doesn't run more than 10 fps. the more this is, the faster it runs
        s.move()

        if s.body[0].pos == snack.pos:
            s.addCube()
            snack = Cube(randomsnack(s), color = (0, 255, 0))
        redrawWindow(wn)

        for i in range(len(s.body)):
            if s.body[i].pos in list(map(lambda z: z.pos, s.body[i+1:])):
                score = len(s.body)
                if score > highscore:
                    highscore = score
                message_box('You lost!', f'High Score : {highscore}\nYour Score : {score}\n Play again...')
                s.reset((10,10))
                break

main()