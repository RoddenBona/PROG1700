import turtle
#setting turtle screem

wn = turtle.Screen()
wn.title("Pong test")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer()

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
ball.penup
ball.goto(0,0)

while True:
    wn.update()