import turtle
from math import pi
turt = turtle.Turtle()

def square(t, length):
    for i in range(4):
        t.fd(length)
        t.lt(90)
        
def poly(t, length, n):
    for i in range(n):
        t.fd(length)
        t.lt(360/n)
        
def circle(t, r):
    ccf = 2*pi*r
    n = 50
    length = ccf/n
    poly(turt, length, n)
    
def arc(t, r, angle):
    arcLen = 2*pi*r*angle/360
    n = int(arcLen/3)+1
    stepLen = arcLen/n
    stepAngle = angle/n
    
    for i in range(n):
        t.fd(stepLen)
        t.lt(stepAngle)
        