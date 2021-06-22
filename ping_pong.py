import turtle

wn = turtle.Screen()
wn.title("Ping Pong by")
wn.bgcolor("black")
wn.setup(width = 800, height = 600)
wn.tracer(0)


    
# Left Paddle
paddle_1 = turtle.Turtle()
paddle_1.speed(0)
paddle_1.shape("square")
paddle_1.color("white")
paddle_1.shapesize(stretch_wid = 5, stretch_len = 1)
paddle_1.penup()
paddle_1.goto(-350,0)

# Right Paddle
paddle_2 = turtle.Turtle()
paddle_2.speed(0)
paddle_2.shape("square")
paddle_2.color("white")
paddle_2.shapesize(stretch_wid = 5, stretch_len = 1)
paddle_2.penup()
paddle_2.goto(350,0)

#Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.x = .5
ball.y = -.5

# Create Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,240)
pen.write("Player A : 0   Player B :  0", align = "center", font = ("Courier", 24 , "bold"))

# Score
score_1 = 0
score_2 = 0

# Move left paddle UP
def paddle_1_up():
    y = paddle_1.ycor()
    y += 20
    paddle_1.sety(y)

# Move left paddle DOWN
def paddle_1_down():
    y = paddle_1.ycor()
    y -= 20
    paddle_1.sety(y)

# Move right paddle UP
def paddle_2_up():
    y = paddle_2.ycor()
    y += 20
    paddle_2.sety(y)

# Move right paddle DOWN
def paddle_2_down():
    y = paddle_2.ycor()
    y -= 20
    paddle_2.sety(y)

wn.listen()
wn.onkeypress(paddle_1_up, "w")
wn.onkeypress(paddle_1_down, "s")
wn.onkeypress(paddle_2_up,"Up")
wn.onkeypress(paddle_2_down,"Down")

while True:
    wn.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.x)
    ball.sety(ball.ycor() + ball.y)

    # Bouncing Upper Wall
    if ball.ycor() > 300 :
        ball.sety(300)
        ball.y *= -1

    # Bouncing Lower Wall
    if ball.ycor() < -300:
        ball.sety(-300)
        ball.y *= -1

    # Re spawn to centre upon right wall collision
    if ball.xcor() > 400 :
        ball.goto(0,0)
        ball.x *= -1
        score_1 += 1
        pen.clear()
        pen.write("Player A : {}   Player B :  {}".format(score_1, score_2), align = "center", font = ("Courier", 24 , "bold"))

        
    # Re spawn to centre upon left wall collision
    if ball.xcor() < -400 :
        ball.goto(0,0)
        ball.x *= -1
        score_2 += 1
        pen.clear()
        pen.write("Player A : {}   Player B :  {}".format(score_1, score_2), align = "center", font = ("Courier", 24 , "bold"))

    # Collision code for right paddle
    if ball.xcor() > 340 and paddle_2.ycor() - 50 < ball.ycor() < paddle_2.ycor() + 50 :
        ball.setx(340)
        ball.x *= -1

    # Collision code for left paddle
    if ball.xcor() < -340 and ball.xcor() > -350 and paddle_1.ycor() - 50 < ball.ycor() < paddle_1.ycor() + 50 :
        ball.setx(-340)
        ball.x *= -1

    # Restricting left paddle to not go off screen(from TOP)
    if paddle_1.ycor() > 250 :
        paddle_1.sety(250)
    
    # Restricting left paddle to not go off screen(from BOTTOM)
    if paddle_1.ycor() < -250 :
        paddle_1.sety(-250)

    # Restricting right paddle to not go off screen(from TOP)
    if paddle_2.ycor() > 250 :
        paddle_2.sety(250)

    # Restricting right paddle to not go off screen(from BOTTOM)
    if paddle_2.ycor() < -250 :
        paddle_2.sety(-250)
