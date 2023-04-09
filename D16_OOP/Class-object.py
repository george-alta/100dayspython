# A class creates objects
# keep this comment
import another_module
from turtle import Turtle, Screen

print(another_module.another_variable)

timmy = Turtle()  # this is to create a timmy object using the turtle class
print(timmy)  # this prints the object to the memory
timmy.shape("turtle")
timmy.color("coral")
# if we create a car object. then car.speed will call the atribute speed from the object car
timmy.forward(100)
timmy.circle(30)
my_screen = Screen()
print(my_screen.canvheight)


# an object has attributes (variables) and methods (functions)
# eg car.stop() will execute the stop method for the car.

my_screen.exitonclick()  # this will allow the program to continue running until a click is detected
