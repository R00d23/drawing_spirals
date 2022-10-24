import turtle
turtle.bgcolor("purple")
turtle.pensize(5)
turtle.speed(0)
## the speed can always be altered using the TUrtle.SPEED( )

for i in range(13):         ## how many times it should iterate
               for  colors in ["red", "green","blue","yellow","pink"] :
                              turtle.color(colors)
                              turtle.circle(150)
                              turtle.left(10)


turtle.hideturtle()
