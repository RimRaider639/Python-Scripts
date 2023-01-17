import turtle
from pygame import mixer, time
mixer.init()
mixer.music.load("sfx-pop.wav")

wn = turtle.Screen()
wn.bgcolor('black')
wn.title('Pong')
wn.setup(width = 800, height = 600)
wn.tracer(0) #speeds up the program

#Paddle A (left)
paddle_a = turtle.Turtle() #instace of Turtle class
paddle_a.speed(0) #sets the animation speed to the max
paddle_a.shape('square')
paddle_a.color('white')
paddle_a.shapesize(stretch_wid=5, stretch_len=1) 
paddle_a.penup() #disallows turtle to trace a line when the object moves
paddle_a.goto(-350, 0) #middle of the screen is (0,0)

#Paddle B (right)
paddle_b = turtle.Turtle() 
paddle_b.speed(0)
paddle_b.shape('square')
paddle_b.color('white')
paddle_b.shapesize(stretch_wid=5, stretch_len=1) 
paddle_b.penup() 
paddle_b.goto(350, 0) 

#Ball
ball = turtle.Turtle()
ball.speed(0) 
ball.shape('circle')
ball.color('white')
ball.penup()
ball.goto(0, 0) 
ball.dx = 0.3 #change in x 
ball.dy = 0.3

#score board
score_a = 0
score_b = 0

pen = turtle.Turtle()
pen.speed(0)
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write('Player A: 0 Player B: 0', align = 'center', font = ('Courier', 24, 'normal'))

#Function
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

#Key binding
wn.listen()
wn.onkeypress(paddle_a_up, 'w')
wn.onkeypress(paddle_a_down, 's')
wn.onkeypress(paddle_b_up, 'Up')
wn.onkeypress(paddle_b_down, 'Down')

#setup
clock = time.Clock()
ballspeed = 300

#main game loop
while True:
    wn.update()
    clock.tick(ballspeed)

    #move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #Border checking
    if ball.ycor() > 290:
        ball.sety(290) #to avoid some issues
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1
        score_b += 1
        pen.clear() #clears the previously written score. Else it will get printed on top.
        pen.write(f'Player A: {score_a} Player B: {score_b}', align = 'center', font = ('Courier', 24, 'normal'))
        ballspeed += 100

    if  ball.ycor() < -290:
        ball.sety(-290) 
        ball.dy *= -1

    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write(f'Player A: {score_a} Player B: {score_b}', align = 'center', font = ('Courier', 24, 'normal'))
        ballspeed += 100

    if paddle_a.ycor() > 250:
        paddle_a.sety(250)

    if paddle_b.ycor() > 250:
        paddle_b.sety(250)

    if paddle_a.ycor() < -250:
        paddle_a.sety(-250)

    if paddle_b.ycor() < -250:
        paddle_b.sety(-250)

    #collisions
    if -340 > ball.xcor() > -350 and paddle_a.ycor() + 50 > ball.ycor() > paddle_a.ycor() - 50:
        ball.setx(-340)
        ball.dx *= -1
        mixer.music.play()

    if 340 < ball.xcor() < 350 and paddle_b.ycor() + 50 > ball.ycor() > paddle_b.ycor() - 50:
        ball.setx(340)
        ball.dx *= -1
        mixer.music.play()