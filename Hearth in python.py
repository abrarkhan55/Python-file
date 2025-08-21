from turtle import *

begin_fill()
color("RED")
left(50)

forward(100)
circle(40,180)
left(260)
circle(40,180)
forward(100)
end_fill()
penup()  # Lift the pen up to move without drawing
goto(-50, -100)  # Move to a suitable position under the heart
pendown()  # Put the pen down to start drawing again

# Write "I love you"
color("black")
write("I love you", font=("Arial", 16, "normal"))
done()