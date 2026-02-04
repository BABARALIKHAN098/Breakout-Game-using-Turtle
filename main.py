import turtle
import random

# Screen setup
wn = turtle.Screen()
wn.title("Breakout - Python Turtle")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Score
score = 0
lives = 3

# Paddle
paddle = turtle.Turtle()
paddle.speed(0)
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=1, stretch_len=5)
paddle.penup()
paddle.goto(0, -250)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("cyan")
ball.penup()
ball.goto(0, -230)
ball.dx = 3
ball.dy = 3

# Bricks
bricks = []
colors = ["red", "orange", "yellow", "green", "blue"]

start_x = -350
start_y = 200

for row in range(5):
    for col in range(10):
        brick = turtle.Turtle()
        brick.speed(0)
        brick.shape("square")
        brick.color(colors[row])
        brick.shapesize(stretch_wid=1, stretch_len=3)
        brick.penup()
        brick.goto(start_x + col * 75, start_y - row * 30)
        bricks.append(brick)

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0  Lives: 3", align="center", font=("Courier", 16, "normal"))

# Paddle movement
def paddle_left():
    x = paddle.xcor()
    if x > -350:
        paddle.setx(x - 30)

def paddle_right():
    x = paddle.xcor()
    if x < 350:
        paddle.setx(x + 30)

wn.listen()
wn.onkeypress(paddle_left, "Left")
wn.onkeypress(paddle_right, "Right")

# Game loop
while True:
    wn.update()

    # Move ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border collisions
    if ball.xcor() > 390 or ball.xcor() < -390:
        ball.dx *= -1

    if ball.ycor() > 290:
        ball.dy *= -1

    # Paddle collision
    if (
        ball.ycor() < -230 and ball.ycor() > -250 and
        ball.xcor() > paddle.xcor() - 60 and
        ball.xcor() < paddle.xcor() + 60
    ):
        ball.dy *= -1

    # Brick collision
    for brick in bricks:
        if brick.isvisible() and ball.distance(brick) < 35:
            brick.hideturtle()
            ball.dy *= -1
            score += 1
            pen.clear()
            pen.write(f"Score: {score}  Lives: {lives}", align="center", font=("Courier", 16, "normal"))

    # Bottom collision
    if ball.ycor() < -290:
        lives -= 1
        pen.clear()
        pen.write(f"Score: {score}  Lives: {lives}", align="center", font=("Courier", 16, "normal"))
        ball.goto(0, -230)
        ball.dy *= -1

        if lives == 0:
            pen.goto(0, 0)
            pen.write("GAME OVER", align="center", font=("Courier", 24, "bold"))
            break

    # Win condition
    if score == len(bricks):
        pen.goto(0, 0)
        pen.write("YOU WIN!", align="center", font=("Courier", 24, "bold"))
        break

wn.mainloop()
