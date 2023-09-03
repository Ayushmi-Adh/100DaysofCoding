#HirstSpotPainting
import turtle as turtle_module
import random
turtle_module.colormode(255)
toby = turtle_module.Turtle()
toby.speed("fastest")
toby.penup()
color_list = [(226, 231, 235), (54, 108, 149), (225, 201, 108), (134, 85, 58), (229, 235, 234), (224, 141, 62), (197, 144, 171), (143, 180, 206), (137, 82, 106), (210, 90, 68), (232, 226, 194), (188, 78, 122), (69, 101, 86), (132, 183, 132), (65, 156, 86), (137, 132, 74), (48, 155, 195), (183, 191, 202), (232, 221, 225), (58, 47, 41), (47, 59, 96), (38, 44, 64), (106, 46, 54), (41, 55, 48), (12, 104, 95), (118, 125, 145), (182, 194, 199), (215, 176, 187), (223, 178, 168), (54, 45, 52)]
toby.setheading((180+270)/2)
toby.forward(300)
toby.setheading(0)
num_dots = 100
for dot in range(1, num_dots + 1):
    toby.dot(20, random.choice(color_list))
    toby.forward(50)

    if dot % 10 == 0:
        toby.setheading(90)
        toby.forward(50)
        toby.setheading(180)
        toby.forward(500)
        toby.setheading(0)









screen = turtle_module.Screen()
screen.exitonclick()

