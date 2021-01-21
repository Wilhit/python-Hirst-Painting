from turtle import Turtle as T, Screen as S
import random

colors = ["grey", "black", "white", "white smoke"]
s = S()
s.colormode(255)
s.bgcolor(random.choice(colors))

# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('hirst.jpg', 30)
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

color_list = [(132, 166, 205), (221, 148, 106), (32, 42, 61), (199, 135, 148), (166, 58, 48), (141, 184, 162),
              (39, 105, 157), (237, 212, 90), (150, 59, 66), (216, 82, 71), (168, 29, 33), (235, 165, 157),
              (51, 111, 90), (35, 61, 55), (156, 33, 31), (17, 97, 71), (52, 44, 49), (230, 161, 166), (170, 188, 221),
              (57, 51, 48), (184, 103, 113), (32, 60, 109), (105, 126, 159), (175, 200, 188), (34, 151, 210),
              (65, 66, 56)]

t = T()
position = 0
movement = 50
t.speed(0)
painting_size = 10


def drawing():
    for _ in range(painting_size):
        for _ in range(painting_size):
            t.dot(20, random.choice(color_list))
            t.forward(movement)
        t.back(painting_size * movement)
        t.left(90)
        t.forward(movement)
        t.right(90)


t.up()
t.hideturtle()
t.setpos(-280.00, -180.00)
drawing()


s.exitonclick()
