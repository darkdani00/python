import turtle


wn = turtle.Screen()

wn.title("Game by Daniel PinBall")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

#paddle A

paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5,stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350,0)

#paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5,stretch_len=1)
paddle_b.penup()
paddle_b.goto(350,0)

#Circle
circle = turtle.Turtle()
circle.speed(1)
circle.shape("circle")
circle.color("white")
circle.penup()
circle.goto(0,0)
circle.dx = 2 #It moves to pixels the ball
circle.dy = -2



#Functions

def paddleA_up():
    y = paddle_a.ycor()
    y += 20 #it adds 20 pixels
    paddle_a.sety(y) #it set the 20 pixels 


def paddleA_down():
    y = paddle_a.ycor()
    y -= 20 #it adds 20 pixels
    paddle_a.sety(y) #it set the 20 pixels 
    
def paddleB_up():
    y = paddle_b.ycor()
    y += 20 #it adds 20 pixels
    paddle_b.sety(y) #it set the 20 pixels 


def paddleB_down():
    y = paddle_b.ycor()
    y -= 20 #it adds 20 pixels
    paddle_b.sety(y) #it set the 20 pixels 
    
    
    
#Keyboard

wn.listen()
wn.onkeypress(paddleA_up, "w")
wn.onkeypress(paddleA_down, "s")
wn.onkeypress(paddleB_up, "Up")
wn.onkeypress(paddleB_down, "Down")


#Main game loop

while True:
    wn.update()
    
    #Ball Movement
    circle.setx(circle.xcor() + circle.dx)
    circle.sety(circle.xcor() + circle.dy)
    
    #limits
    
    if circle.ycor() > 290:
        circle.sety(290)
        circle.dy *= -1
    
    if circle.ycor() < -290:
        circle.sety(-290)
        circle.dy *= -1
    
    if circle.xcor() > 390:
        circle.goto(0,0)
        circle.dx *= -1
    
    
    if circle.xcor() < -390:
        circle.goto(0,0)
        circle.dx *= -1    