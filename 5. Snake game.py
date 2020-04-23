import turtle
import random
import time

delay=0.1
score=0
highscore=0
#Create a screen
screen = turtle.Screen()
screen.title("Snake Game")
screen.bgcolor("blue")
screen.setup(600,600)
screen.tracer(0) #Turns off screen updates

#Create snake head
head = turtle.Turtle() #Needs to have the () at the end, or else attribute error
head.speed(0) #Animation speed, not speed of the head
head.shape("square")
head.color("white", "green")
head.penup()
head.goto(0,0)
head.direction = "stop"

#Create Snake food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(100,0)
food.direction= "stop"

segments = []

#Create a pen
pen= turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write(("Score: 0 HighScore: 0"), align = "center", font =("Arial", 14, "normal"))


#Functions
def move(): #To move the snake head
    if head.direction == "up":
        y = head.ycor()
        head.sety(y+20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y-20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x-20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x+20)

def go_up(): #To change direction of snake head
    if head.direction != "down":
        head.direction = "up"
def go_down():
    if head.direction != "up":
        head.direction = "down"
def go_left():
    if head.direction != "right":
        head.direction = "left"
def go_right():
    if head.direction != "left":
        head.direction = "right"

#Keyboard bindings
screen.listen()
screen.onkeypress(go_up, "Up")
screen.onkeypress(go_down, "Down")
screen.onkeypress(go_left, "Left")
screen.onkeypress(go_right, "Right")

#Main loop
while True:
    screen.update() #Updates screen so there is animation
    #Check for collision with border
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"
        #Hide segments
        for segment in segments:
            segment.goto(1000,1000)
        #Clear the segments
        segments.clear()

        score = 0
        pen.clear()
        pen.write(("Score: {} HighScore: {}").format(score, highscore), align = "center", font =("Arial", 14, "normal"))

    if head.distance(food)<20:
        food.goto(random.randrange(-290,290), random.randrange(-280,260))
        score += 10

        #Add a segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)

        #Check the score
        if score>highscore:
            highscore=score

        pen.clear()
        pen.write(("Score: {} HighScore: {}").format(score, highscore), align= "center", font=("Arial",14, "normal"))

    #Move the segments in reverse order
    for index in range(len(segments)-1,0,-1):
        x = segments[index-1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x,y)

    #Move segment 0 to where the head is
    if len(segments) > 0:
        segments[0].goto(head.xcor(),head.ycor())

    move()

    #Check for head collision with body segments
    for segment in segments:
        if head.distance(segment) < 20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"

            for segment in segments:
                segment.goto(1000,1000)
            segments.clear()
            score = 0

        pen.clear()
        pen.write(("Score: {} HighScore: {}").format(score, highscore), align = "center", font = (
        "Arial", 14, "normal"))

    time.sleep(delay)


screen.mainloop() #Keep windows open