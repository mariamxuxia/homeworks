# 3)შექმენით ფუნქცია, რომელიც ხატავს ოთხუკთედს Turtle ბიბლიოკეთის გამოყენებით
from turtle import *
def aham():
    speed(0)
    forward(50)
    left(90)
    forward(50)
    left(90)
    forward(50)
    left(90)
    forward(50)
    exitonclick()
    aham()