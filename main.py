import turtle as turtule_module
import random

turtule_module.colormode(255)
hirst = turtule_module.Turtle()
hirst.speed("fastest")
hirst.penup()
hirst.hideturtle()

color_list = []

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

for _ in range(30):
    color = random_color()
    color_list.append(color)

hirst.setheading(225)
hirst.forward(300)
hirst.setheading(0)
number_of_dots = 100


for dot_count in range (1, number_of_dots + 1):
    hirst.dot(20, random.choice(color_list))
    hirst.forward(50)

    if dot_count % 10 == 0:
        hirst.setheading(90)
        hirst.forward(50)
        hirst.setheading(180)
        hirst.forward(500)
        hirst.setheading(0)




screen = turtule_module.Screen()
screen.exitonclick()