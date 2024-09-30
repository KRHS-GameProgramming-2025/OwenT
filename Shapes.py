from turtle import *
from math import *


def equilateral_tri(t, size=100, rotate=0, lineColor=None, fillColor=None):
    print ("Equilateral Triangle, with Size:", size, "and Rotation:", rotate)
    if lineColor != None:
        p = t.pencolor()
        t.pencolor(lineColor)
    if fillColor != None:
        f = fillcolor()
        t.fillcolor(fillColor)
        t.begin_fill()
    t.lt(rotate)
    count = 0;
    while count < 3:
      t.fd(size)
      t.lt(120)
      count = count + 1
    t.rt(rotate)
    if fillColor != None:
        t.end_fill()
        t.fillcolor(f)
    if lineColor != None:
        t.pencolor(p)

#--------------------------QUADRILATERALS-------------------------#

def para(t, width=100, height=100, big_angle=120, rotate=0, lineColor=None, fillColor=None):
    print ("Parallelogram, with Width:", width, "Height:", height, "Large Angle:", big_angle, "and Rotation:", rotate)
    if lineColor != None:
        p = t.pencolor()
        t.pencolor(lineColor)
    if fillColor != None:
        f = fillcolor()
        t.fillcolor(fillColor)
        t.begin_fill()
    t.lt(rotate)
    count = 0;
    while count < 2:
        t.fd(width)
        t.lt(big_angle)
        t.fd(height)
        t.lt(180 - big_angle)
        count = count + 1
    t.rt(rotate)
    if fillColor != None:
        t.end_fill()
        t.fillcolor(f)
    if lineColor != None:
        t.pencolor(p)

def rhom(t, size=100, big_angle=120, rotate=0, lineColor=None, fillColor=None):
    print ("Rhombus, with Size:", size, "Large Angle:", big_angle, "and Rotation:", rotate)
    para(t, size, size, big_angle, rotate, lineColor, fillColor)
        
def rect(t, width=100, height=100, rotate=0, lineColor=None, fillColor=None):
    print ("Rectangle, with Width:", width, "Height:", height, "and Rotation:", rotate)
    para(t, width, height, 90,rotate, lineColor, fillColor)
    
def square(t, size=100, rotate=0, lineColor=None, fillColor=None):
    print ("Sqaure, with Size:", size, "and Rotation:", rotate)
    para(t, size, size, 90, rotate, lineColor, fillColor)
#-------------------------------POLYGONS--------------------------#

def poly(t, sides=5, size=100, rotate=0, lineColor=None, fillColor=None):
    print ("Polygon, with Sides:", sides, "Size:", size, "and Rotation:", rotate)
    if lineColor != None:
        p = t.pencolor()
        t.pencolor(lineColor)
    if fillColor != None:
        f = fillcolor()
        t.fillcolor(fillColor)
        t.begin_fill()
    t.lt(rotate)
    count = 0;
    while count < sides:
        t.fd(size)
        t.lt(360/sides)
        count += 1
    t.rt(rotate)
    if fillColor != None:
        t.end_fill()
        t.fillcolor(f)
    if lineColor != None:
        t.pencolor(p)
    
    
def star(t, points=5, size=100.0, rotate=0, lineColor=None, fillColor=None):
    print ("Star, with Points:", points, "Size:", size, "and Rotation:", rotate)
    if lineColor != None:
        p = t.pencolor()
        t.pencolor(lineColor)
    if fillColor != None:
        f = fillcolor()
        t.fillcolor(fillColor)
        t.begin_fill()
    t.lt(rotate)
    count = 0;
    while count < points:
        t.fd(size)
        t.lt(180-(180-2*(360/points)))
        count += 1
    t.rt(rotate)
    if fillColor != None:
        t.end_fill()
        t.fillcolor(f)
    if lineColor != None:
        t.pencolor(p)

#------------------------------MOVEMENT---------------------------#

def line(t, x=100, y=100, lineColor=None):
    print ("Line to a point X:", x, "over and Y:", y, "up")
    if lineColor != None:
        p = t.pencolor()
        t.pencolor(lineColor)
    angle = degrees(atan(y/x))
    dist = sqrt(x**2 + y**2)
    t.lt(angle)
    t.fd(dist)
    t.rt(angle)
  
def move(t, x, y):
    print ("Move without marking a line to a point X:", x, "over and Y:", y, "up")
    t.pu()
    line(t,x,y)
    t.pd()
 
