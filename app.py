import turtle, time, random

DELAY = 0.15
fen = turtle.Screen()
fen.title("Snake Game")
fen.tracer(0)
head = turtle.Turtle()
head.shape("square")
head.color("red")
head.penup()
head.goto(0, 0)
head.direction = "stop"

segments = []

food = turtle.Turtle()
food.shape("circle")
food.color("green")
food.penup()
food.goto(0, 100)


pen = turtle.Turtle()
pen.hideturtle()
pen.color("white")
pen.penup()


game_over = False
score = 0

def go_up():
    head.direction = "up"

def go_down():
    head.direction = "down"

def go_left():
    head.direction = "left"

def go_right():
    head.direction = "right"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)
fen.listen()
fen.onkey(go_up, "Up")
fen.onkey(go_down, "Down")
fen.onkey(go_left, "Left")
fen.onkey(go_right, "Right")
while not game_over:
    fen.update()


    if abs(head.xcor()) > 290 or abs(head.ycor()) > 290:
        game_over = True


    if head.distance(food) < 20:
        score += 10
        food.goto(random.randint(-14,14) * 20, random.randint(-14,14) * 20)
        seg= turtle.Turtle()
        seg.shape("square")
        seg.color("red")
        seg.penup()
        segments.append(seg)


    for i in range(len(segments)-1, 0, -1):
        segments[i].goto(segments[i-1].xcor(), segments[i-1].ycor())


    if len(segments) > 0:
        segments[0].goto(head.xcor(), head.ycor())

    move()


    for segment in segments:
        if head.distance(segment) < 20:
            game_over = True
    
    time.sleep(DELAY)


if game_over:
    pen.goto(0, 0)
    pen.write(f"Game Over\nScore: {score}", align="center", font=("Courier", 24, "normal"))

fen.mainloop()