import turtle
def draw_heart():
    turtle.color('red')  
    turtle.begin_fill()
    turtle.left(140)
    turtle.forward(220)
    for _ in range(200): 
        turtle.right(1)
        turtle.forward(2)
    turtle.left(120)
    for _ in range(200):
        turtle.right(1)
        turtle.forward(2)
    turtle.forward(220)
    turtle.end_fill()

def draw_text():
    turtle.penup()
    turtle.goto(0, 80)  
    turtle.color('white') 
    turtle.write("FELIZ SAN VALENTÍN", align="center", font=("Arial", 20, "bold"))
    turtle.goto(0, 30) 
    turtle.write("Te Amo", align="center", font=("Arial", 20, "bold"))  

turtle.speed(18) 
turtle.bgcolor("white")  
turtle.penup()
turtle.goto(0, -100)
turtle.pendown()

draw_heart()  # Dibuja el corazón
draw_text()   # Dibuja los textos

turtle.hideturtle()
turtle.done()
