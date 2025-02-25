# import turtle
# import math
# def draw_book():
#     turtle.penup()
#     turtle.goto(-130, -50)
#     turtle.pendown()
#     turtle.color("darkolivegreen")
#     turtle.begin_fill()
#     turtle.goto(130, -50)
#     turtle.goto(110, -30)
#     turtle.goto(-110, -30)
#     turtle.goto(-130, -50)
#     turtle.end_fill()
    
#     turtle.penup()
#     turtle.goto(-110, -30)
#     turtle.pendown()
#     turtle.color("olive")
#     turtle.begin_fill()
#     turtle.goto(110, -30)
#     turtle.goto(115, -20)
#     turtle.goto(-115, -20)
#     turtle.goto(-110, -30)
#     turtle.end_fill()

#     turtle.color("black")
#     for i in range(-100, 101, 20):
#         turtle.penup()
#         turtle.goto(i, -30)
#         turtle.pendown()
#         turtle.goto(i+10, -20)

# def draw_light_bulb():
#     turtle.penup()
#     turtle.goto(-20, -40)
#     turtle.pendown()
#     turtle.color("darkolivegreen")
#     turtle.begin_fill()
#     turtle.goto(20, -40)
#     turtle.goto(10, -30)
#     turtle.goto(-10, -30)
#     turtle.goto(-20, -40)
#     turtle.end_fill()

# def draw_brain():
#     turtle.penup()
#     turtle.goto(0, 50)
#     turtle.pendown()
#     turtle.color("gold")
#     turtle.begin_fill()
#     for i in range(361):
#         x = 50 * math.sin(math.radians(i))
#         y = 30 * math.cos(math.radians(i))
#         turtle.goto(x, y + 50)
#     turtle.end_fill()

# def draw_brain_lines():
#     turtle.color("black")
#     turtle.penup()
#     turtle.goto(0, 80)
#     turtle.pendown()
#     turtle.goto(0, 20)
    
#     for i in range(-2, 3):
#         turtle.penup()
#         turtle.goto(i * 10, 70)
#         turtle.pendown()
#         turtle.goto(i * 15, 50)

# def draw_rays():
#     turtle.color("gold")
#     for angle in range(0, 360, 20):
#         turtle.penup()
#         x = 70 * math.cos(math.radians(angle))
#         y = 70 * math.sin(math.radians(angle)) + 50
#         turtle.goto(0, 50)
#         turtle.pendown()
#         turtle.goto(x, y)

# def draw_text():
#     turtle.penup()
#     turtle.goto(0, -80)
#     turtle.color("black")
#     turtle.write("-ملتقى القران الكريم -الجامعة العربية الأمريكية", align="center", font=("Arial", 16, "bold"))

# def draw_logo():
#     turtle.speed(0)
#     draw_book()
#     draw_light_bulb()
#     draw_brain()
#     draw_brain_lines()
#     draw_rays()
#     draw_text()
#     turtle.hideturtle()
#     turtle.done()

# draw_logo()


import math 
from turtle import *
def heart(k):
    return 15 * math.sin(k) ** 3
def heart1(k):
    return 12 * math.cos(k) - 5 * \
           math.cos(2 * k) - 2 * \
            math.cos(3 * k) - \
            math.cos(4 * k)
speed('fastest')  
bgcolor('#000000')
tracer(0)
penup()
for i in range(6000): 
    goto(heart(i)*20, heart1(i)*20)
    color('pink')
    pendown()
update()
penup()
goto(-10, -50)  
color('pink')
write("نور", align="center", font=("Arial", 40, "normal"))
done()






# import math
# from turtle import *
# def heart(k):
#     return 15 * math.sin(k) ** 3
# def heart1(k):
#     return 12 * math.cos(k) - 5 * \
#            math.cos(2 * k) - 2 * \
#             math.cos(3 * k) - \
#             math.cos(4 * k)

# speed(1000)
# bgcolor('black')

# for i in range(6000):
#     goto(heart(i)*20,heart1(i)*20)
#     for j in range(5):
#         color('pink')
# done()