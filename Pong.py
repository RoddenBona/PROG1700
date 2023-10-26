import turtle
#setting turtle screem

score_one = 0
score_two = 0

wn = turtle.Screen()
wn.title("Pong test")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

paddle_one = turtle.Turtle()
paddle_one.shape("square")
paddle_one.color("white")
paddle_one.speed(0)
paddle_one.shapesize(stretch_wid=5,stretch_len=1)
paddle_one.penup()
paddle_one.goto(-350,0)

paddle_two = turtle.Turtle()
paddle_two.shape("square")
paddle_two.color("white")
paddle_two.speed(0)
paddle_two.shapesize(stretch_wid=5,stretch_len=1)
paddle_two.penup()
paddle_two.goto(350,0)

ball = turtle.Turtle()
ball.shape("square")
ball.color("white")
ball.speed(0)
ball.penup()
ball.goto(0,0)

Scoreboard = turtle.Turtle()
Scoreboard.speed(0)
Scoreboard.color("black")
Scoreboard.penup()
Scoreboard.goto(0,260)
Scoreboard.color("white")
Scoreboard.write("Player One:{} Player Two: {}".format(score_one, score_two), align="center", font=("Courier", 24, "normal"))
Scoreboard.hideturtle()

def paddle_one_up():
    y = paddle_one.ycor()
    y += 20
    paddle_one.sety(y)

def paddle_one_down():
    y = paddle_one.ycor()
    y -= 20
    paddle_one.sety(y)

def paddle_two_up():
    y = paddle_two.ycor()
    y += 20
    paddle_two.sety(y)

def paddle_two_down():
    y = paddle_two.ycor()
    y -= 20
    paddle_two.sety(y)

wn.listen()
wn.onkeypress(paddle_one_up, "w")
wn.onkeypress(paddle_one_down, "s")
wn.onkeypress(paddle_two_up, "o")
wn.onkeypress(paddle_two_down, "k")

play = True
while play:
    wn.update()

