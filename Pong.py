# Pong in Python

import turtle

win = turtle.Screen()
win.title("Pong in Python")
win.bgcolor("black")
win.setup(width=800, height=600)
win.tracer(0)

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0) # The speed of animation.
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1) # Stretching the paddle to be 100px by 20px. By default the paddle is 20px by 20px.
paddle_a.penup()
paddle_a.goto(-350, 0) # Positioning the paddle along the x and y axes.


# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.2 # Ball moves by 2px to the right
ball.dy = -0.2 # Ball moves by 2px to the top

# Creating the score table
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("PlayerA: 0  PlayerB: 0", align="center", font=("Arial", 24, "normal"))

# Score
score_a = 0
score_b = 0


# Function
def paddle_a_up(): # Moving the paddle up
    y = paddle_a.ycor() # Return the y coord
    y+= 20 # Increase the y coord. by 20
    paddle_a.sety(y) # Set the y coord. to the new y

def paddle_a_down():
    y = paddle_a.ycor()
    y-= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y+= 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y-= 20
    paddle_b.sety(y)

# Keyboard binding (Moving the paddle using the keyboard)
win.listen()
win.onkeypress(paddle_a_up, "w")
win.onkeypress(paddle_a_down, "s")
win.onkeypress(paddle_b_up, "Up")
win.onkeypress(paddle_b_down, "Down")

# Game loop
while True:
    win.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.ycor() > 290: # Initial we have 600 height, so first half of the screen is 300 and second half is 300, and also the ball is 20X20.
        ball.sety(290)
        ball.dy *= -1 # Reverse the direction of the ball

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390: # When the ball hits the right side, then reset.
        ball.goto(0, 0)
        ball.dx *= -1
        score_a +=1
        pen.clear()
        pen.write("PlayerA: {}  PlayerB: {}".format(score_a, score_b), align="center", font=("Arial", 24, "normal")) # Counting the score

    if ball.xcor() < -390: # When the ball hits the left side, then reset.
        ball.goto(0, 0)
        ball.dx *= -1
        score_b +=1
        pen.clear()
        pen.write("PlayerA: {}  PlayerB: {}".format(score_a, score_b), align="center", font=("Arial", 24, "normal"))

    # Ball bouncing

    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() -40):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() -40):
        ball.setx(-340)
        ball.dx *= -1

