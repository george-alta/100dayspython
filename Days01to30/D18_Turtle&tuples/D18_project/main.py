import turtle as turtle_module
import random
turtle_module.colormode(255)
# import colorgram

# rgb_colors = []
# colors = colorgram.extract("D18_Turtle&tuples/D18_project/image.jpg", 10)

# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)

# print(rgb_colors)
tim = turtle_module.Turtle()
tim.penup()
tim.speed("fastest")
tim.hideturtle()
color_list = [(132, 166, 205), (221, 148, 106), (32, 42, 61),
              (199, 135, 148), (166, 58, 48), (141, 184, 162)]

# 10 x 10 spots, each one in size 20, spaced 50

tim.setpos(-200, -200)
for line in range(10):
    for i in range(10):
        tim.dot(20, random.choice(color_list))
        tim.forward(50)
    tim.setx(tim.xcor()-500)
    tim.sety(tim.ycor()+50)


# tim.goto(60, 30)


screen = turtle_module.Screen()
screen.exitonclick()

# setx(x)
# sety(y)
# xcor()
# ycor()
