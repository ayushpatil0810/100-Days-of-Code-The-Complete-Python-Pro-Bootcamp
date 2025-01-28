# Day 19
import turtle
from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def moves_forward():
    tim.forward(10)

def moves_backward():
    tim.backward(10)

def turn_left():
    tim.left(10)

def turn_right():
    tim.right(10)

screen.listen()
screen.onkey(key="w", fun=moves_forward)
screen.onkey(key="s", fun=moves_backward)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=screen.reset)

screen.exitonclick()