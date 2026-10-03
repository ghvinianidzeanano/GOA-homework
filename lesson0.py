from turtle import*

#we want to paint a house

#step 1: draw a square

width(8)
color("navy")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

#end of square 

#drawing a door

forward(70)

color("orange")
begin_fill()
left(90)
forward(120) #height of the door
right(90)
forward(60)
right(90)
forward(120)
penup()
end_fill()

penup()
goto(200, 200)
pendown()

color("darkred")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

#end of the door

#drawing left window

penup()
goto(30, 130)
left(210)
pendown()
color("skyblue")

begin_fill()
forward(40)
right(90)
forward(40)
right(90)
forward(40)
right(90)
forward(40)
right(90)
end_fill()

#drawing right window
penup()
goto(130,130)
pendown()


begin_fill()
forward(40)
right(90)
forward(40)
right(90)
forward(40)
right(90)
forward(40)
right(90)
end_fill()

exitonclick()