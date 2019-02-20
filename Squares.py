import turtle
def draw_square():
    brad  = turtle.Turtle()
    brad.shape("turtle")
    brad.color("yellow")
    brad.speed("fast")
    performCircle = 40
    makeSquare = 4
    while performCircle > 0:
        for createSquare in range(makeSquare):
            brad.forward(100)
            brad.right(90)
        brad.right(10)
        performCircle = performCircle - 1




# def draw_cirle():
    #angie = turtle.Turtle()
    #angie.shape("circle")
    #angie.color("white")
    #angie.speed("slowest")
    #angie.circle(100)

#def draw_triangle():
    #natalie = turtle.Turtle()
    #natalie.shape("triangle")
    #natalie.color("blue")
    #natalie.speed("slowest")
    #makeSquare = 3
    #for createSquare in range(makeSquare):
        #natalie.forward(120)
        #natalie.left(120)

def draw_shape():
    window = turtle.Screen()
    window.bgcolor("red")
    draw_square()
    window.exitonclick()

draw_shape()
