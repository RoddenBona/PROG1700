import turtle
#setting turtle screem

#player scores
score_one = 0
score_two = 0

#Set default screen size
wn = turtle.Screen()
wn.title("Pong test")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

#player one's paddle
paddle_one = turtle.Turtle()
paddle_one.shape("square")
paddle_one.color("yellow")
paddle_one.speed(0)
paddle_one.shapesize(stretch_wid=5,stretch_len=1)
paddle_one.penup()
paddle_one.goto(-350,0)

#player two's paddle
paddle_two = turtle.Turtle()
paddle_two.shape("square")
paddle_two.color("purple")
paddle_two.speed(0)
paddle_two.shapesize(stretch_wid=5,stretch_len=1)
paddle_two.penup()
paddle_two.goto(350,0)

#Ball drawing and movement
ball = turtle.Turtle()
ball.shape("circle")
ball.color("red")
ball.speed(0)
ball.penup()
ball.goto(0,0)
ball.dx = -0.05
ball.dy = -0.05

#draw the scoreboard
Scoreboard = turtle.Turtle()
Scoreboard.speed(0)
Scoreboard.color("black")
Scoreboard.penup()
Scoreboard.goto(0,260)
Scoreboard.color("white")
Scoreboard.write("Player One:{} Player Two: {}".format(score_one, score_two), align="center", font=("Courier", 24, "normal"))
Scoreboard.hideturtle()

#player one movement
def paddle_one_up():
    y = paddle_one.ycor()
    y += 20
    paddle_one.sety(y)

def paddle_one_down():
    y = paddle_one.ycor()
    y -= 20
    paddle_one.sety(y)

#player two movement
def paddle_two_up():
    y = paddle_two.ycor()
    y += 20
    paddle_two.sety(y)

def paddle_two_down():
    y = paddle_two.ycor()
    y -= 20
    paddle_two.sety(y)

#Keyboard mapping. arrow keys need to be capitalized
wn.listen()
wn.onkeypress(paddle_one_up, "w")
wn.onkeypress(paddle_one_down, "s")
wn.onkeypress(paddle_two_up, "Up")
wn.onkeypress(paddle_two_down, "Down")

#main
play = True
while play:
    wn.update()
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

#Check top and bottom borders
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy = ball.dy * -1
    elif ball.ycor() < -290:
        ball.sety(-290)
        ball.dy = ball.dy * -1
    
    #Check left and right borders
    if ball.xcor() > 390:
        #score_one = score_one + 1 also would work here as well
        score_one =+ 1
        Scoreboard.clear()
        Scoreboard.write("Player One:{} Player Two: {}".format(score_one, score_two), align="center", font=("Courier", 24, "normal"))
        ball.goto(0,0)
    elif ball.xcor() < -390:
        score_two =+ 1
        Scoreboard.clear()
        Scoreboard.write("Player One:{} Player Two: {}".format(score_one, score_two), align="center", font=("Courier", 24, "normal"))
        ball.goto(0,0)

#paddle and ball collision
    if ball.xcor() < -340 and ball.ycor() < paddle_one.ycor() + 50 and ball.ycor() > paddle_one.ycor() - 50:
        ball.setx(-340)
        ball.dx = ball.dx * -1
    elif ball.xcor() > 340 and ball.ycor() < paddle_two.ycor() + 50 and ball.ycor() > paddle_two.ycor() - 50:
        ball.setx(340)
        ball.dx = ball.dx * -1