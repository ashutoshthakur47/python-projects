import turtle

make = turtle.Turtle()
make.speed(15)

#orange strip
make.penup()
make.goto(-400,380)
make.pendown()
make.fillcolor("orange")
make.begin_fill()
make.forward(800)
make.right(90)
make.forward(200)
make.right(90)
make.forward(800)
make.right(90)
make.forward(200)
make.end_fill()

#green strip
make.penup()
make.goto(-400,-20)
make.pendown()
make.fillcolor("green")
make.begin_fill()
make.right(90)
make.forward(800)
make.right(90)
make.forward(200)
make.right(90)
make.forward(800)
make.right(90)
make.forward(200)
make.end_fill()

#white strip
make.forward(200)
make.right(90)
make.forward(800)
make.right(90)
make.forward(200)
make.right(90)
make.forward(800)
make.right(90)
make.forward(200)

#blue circle
make.right(90)
make.forward(400)
make.right(180)
make.width(5)
make.pencolor("navy")
make.circle(100)
    
#ashoka chakra
make.penup()
make.goto(0,80)
make.pendown()
for i in range(24):
    make.width(2)
    make.forward(100)
    make.penup()
    make.goto(0,80)
    make.pendown()
    make.right(15)


turtle.done()


