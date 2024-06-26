from turtle import *

header_text = "Para ti con todo mi amor"
color("white")
penup()
goto(-100, 250)
pendown()
write(header_text, align="left", font=("Arial", 12, "normal"))

speed(20)
bgcolor("black")
h = 0

penup()
goto(0, -100)
pendown()
color("green")
begin_fill()
rt(90)
fd(400)
lt(90)
fd(20)
lt(90)
fd(400)
lt(90)
fd(20)
end_fill()

penup()
goto(0, 0)
pendown()
for i in range(16):
    for j in range(10):
        color("yellow")
        h += 0.005
        rt(90)
        circle(150 - j * 6, 90)
        lt(90)
        circle(150 - j * 6, 90)
        rt(180)
    circle(40, 24)

penup()
goto(-20, 0)
pendown()
color("brown")
begin_fill()
circle(44)
end_fill()

exitonclick()  # Cierra la ventana al hacer clic en ella
