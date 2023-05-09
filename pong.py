# The classic Pong in python

import turtle

wn = turtle.Screen()
wn.title("Pong by Caio Rezende")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer
wn.tracer(0)

# Score
score_a = 0
score_b = 0

# Paddle 1 (left side)
paddle1 = turtle.Turtle()
paddle1.speed(0)
paddle1.shape("square")
paddle1.shapesize(stretch_wid=5, stretch_len=1)
paddle1.color("white")
paddle1.penup()
paddle1.goto(-350, 0)

# Paddle 2 (rigth side)
paddle2 = turtle.Turtle()
paddle2.speed(0)
paddle2.shape("square")
paddle2.shapesize(stretch_wid=5, stretch_len=1)
paddle2.color("white")
paddle2.penup()
paddle2.goto(350, 0)


# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.1
ball.dy = -0.1

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player b: 0", align="center",
          font=("Courier", 24, "normal"))


# Moviments
def paddle1_up():
    y = paddle1.ycor()
    y += 40
    paddle1.sety(y)


def paddle1_down():
    y = paddle1.ycor()
    y -= 40
    paddle1.sety(y)


def paddle2_up():
    y = paddle2.ycor()
    y += 40
    paddle2.sety(y)


def paddle2_down():
    y = paddle2.ycor()
    y -= 40
    paddle2.sety(y)

# ball velocity


def ballVelo1():
    ball.dx = 0.1
    ball.dy = -0.1


def ballVelo2():
    ball.dx = 0.2
    ball.dy = -0.2


# Theme table
def colorTheme_blue():
    wn.bgcolor("royal blue")


def colorTheme_black():
    wn.bgcolor("black")


# Keyboard biding
wn.listen()
wn.onkeypress(paddle1_up, "w")
wn.onkeypress(paddle1_down, "s")

wn.onkeypress(paddle2_up, "Up")
wn.onkeypress(paddle2_down, "Down")

wn.onkeypress(colorTheme_blue, "c")
wn.onkeypress(colorTheme_black, "v")

wn.onkeypress(ballVelo1, "1")
wn.onkeypress(ballVelo2, "2")


# game loop
while True:
    wn.update()

    # ball movement
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Ball checking up and down border
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    # Ball checking right and left border
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  Player b: {}" .format(
            score_a, score_b), align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player b: {}" .format(
            score_a, score_b), align="center", font=("Courier", 24, "normal"))

    # Paddle and ball collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle2.ycor() + 40 and ball.ycor() > paddle2.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle1.ycor() + 40 and ball.ycor() > paddle1.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1
