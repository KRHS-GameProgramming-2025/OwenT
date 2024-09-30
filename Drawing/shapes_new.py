from turtle import *
from math import *

#-------------------------OTHER FUNCTIONS-------------------------#
  
def law_of_cosines(adj1, adj2, opp):
  ang=degrees(acos(((adj1**2)+(adj2**2)-(opp**2))/(2*adj1*adj2)))
  return ang
  
#----------------------------TRIANGLES----------------------------#
 
def equilateral_tri(t, size=100, rotate=0, line_color=None, fill_color=None):
    print("Equilateral Triangle, with Size:", size, "and Rotation:", rotate, "with", line_color, "lines and", fill_color, "fill")
    tri(t, size, size, size, rotate, line_color, fill_color)
  
def right_tri(t, base=100, height=50, rotate=0, line_color=None, fill_color=None):
    print("Right Triangle, with Base:", base, "Height:", height, "and Rotation:", rotate, "with", line_color, "lines and", fill_color, "fill")
    hyp=sqrt((base*base)+(height*height))
    tri(t, base, height, hyp, rotate, line_color, fill_color) 

def sss_tri(t, side1=100, side2=50, side3=75, rotate=0, line_color=None, fill_color=None):
    #Based on function by tucker tibbetts
    print("SSS Triangle, with Sides:", side1, side2, side3, "and Rotation:", rotate, "with", line_color, "lines and", fill_color, "fill")
    sides=[side1,side2,side3]
    sides.sort()
    if sides[2]>sides[0]+sides[1]:
        print("\tBad Triangle!")
        return
    t.lt(rotate)
    if fill_color != None:
        fc = t.fillcolor()
        t.fillcolor(fill_color)
        t.begin_fill()
    if line_color != None:
        lc = t.pencolor()
        t.pencolor(line_color)
    ang1=180-law_of_cosines(side1, side2, side3)
    ang2=180-law_of_cosines(side2, side3, side1)
    ang3=180-law_of_cosines(side1, side3, side2)
    t.fd(side1)                         
    t.lt(ang1)
    t.fd(side2)
    t.lt(ang2)
    t.fd(side3)
    t.lt(ang3)  
    t.rt(rotate)
    if line_color != None:
        t.pencolor(lc)
    if fill_color != None:
        t.end_fill()
        t.fillcolor(fc)
    
def tri(t, side1=100, side2=50, side3=75, rotate=0, line_color=None, fill_color=None):
    sss_tri(t, side1, side2, side3, rotate, line_color, fill_color)
    
#--------------------------QUADRILATERALS-------------------------#

def para(t, width=100, height=100, big_angle=120, rotate=0, line_color=None, fill_color=None):
    print("Parallelogram, with Width:", width, "Height:", height, "Large Angle:", big_angle, "and Rotation:", rotate, "with", line_color, "lines and", fill_color, "fill")
    if fill_color != None:
        fc = t.fillcolor()
        t.fillcolor(fill_color)
        t.begin_fill()
    if line_color != None:
        lc = t.pencolor()
        t.pencolor(line_color)
    small_angle=180-big_angle
    t.lt(rotate)
    t.fd(width)
    t.lt(small_angle)
    t.fd(height)
    t.lt(big_angle)
    t.fd(width)
    t.lt(small_angle)
    t.fd(height)
    t.lt(big_angle)
    t.rt(rotate) 
    if line_color != None:
        t.pencolor(lc)
    if fill_color != None:
        t.end_fill()
        t.fillcolor(fc)

def rhom(t, size=100, big_angle=120, rotate=0, line_color=None, fill_color=None):
    print("Rhombus, with Size:", size, "Large Angle:", big_angle, "and Rotation:", rotate, "with", line_color, "lines and", fill_color, "fill")
    para(t, size, size, big_angle, rotate, line_color, fill_color)
  
def rect(t, width=100, height=100, rotate=0, line_color=None, fill_color=None):
    print("Rectangle, with Width:", width, "Height:", height, "and Rotation:", rotate, "with", line_color, "lines and", fill_color, "fill")
    para(t, width, height, 90, rotate, line_color, fill_color)

def square(t, size=100, rotate=0, line_color=None, fill_color=None):
    print("Sqaure, with Size:", size, "and Rotation:", rotate, "with", line_color, "lines and", fill_color, "fill")
    para(t, size, size, 90, rotate, line_color, fill_color)
  
#-------------------------------POLYGONS--------------------------#

def poly(t, sides=5, size=100, rotate=0, line_color=None, fill_color=None):
    print("Polygon, with Sides:", sides, "Size:", size, "and Rotation:", rotate, "with", line_color, "lines and", fill_color, "fill")
    if fill_color != None:
        fc = t.fillcolor()
        t.fillcolor(fill_color)
        t.begin_fill()
    if line_color != None:
        lc = t.pencolor()
        t.pencolor(line_color)
    t.lt(rotate)
    angle = 360.0/sides
    count=1
    while count<=sides:
        t.fd(size)
        t.lt(angle)
        count+=1
    t.rt(rotate) 
    if line_color != None:
        t.pencolor(lc)
    if fill_color != None:
        t.end_fill()
        t.fillcolor(fc)

def star(t, points=5, size=100.0, rotate=0, line_color=None, fill_color=None):
    #Based on function by zander blasingame
    print("Star, with Points:", points, "Size:", size, "and Rotation:", rotate, "with", line_color, "lines and", fill_color, "fill")
    if fill_color != None:
        fc = t.fillcolor()
        t.fillcolor(fill_color)
        t.begin_fill()
    if line_color != None:
        lc = t.pencolor()
        t.pencolor(line_color)
    t.lt(rotate)
    for i in range(points):
            t.fd(size)
            t.rt(720/float(points))
    t.rt(rotate)  
    if line_color != None:
        t.pencolor(lc)
    if fill_color != None:
        t.end_fill()
        t.fillcolor(fc) 

#------------------------------MOVEMENT---------------------------#

def line(t, x=100, y=100, line_color=None):
    print("Line to a point X:", x, "over and Y:", y, "up", "in", line_color)
    if line_color != None:
        lc = t.pencolor()
        t.pencolor(line_color)
    x=float(x)
    y=float(y)
    if x!=0 and y!=0: #Not on an Axis
        hyp=sqrt(x**2+y**2)
        angle=degrees(atan(y/x))
    elif x==0: #On X Axis
        angle=90
        hyp=y
    else:   #On Y Axis
        angle=0
        hyp=x
        
    if x<0 and y<0: #Quad 3
        angle=angle-180
    elif x<0 and y>0: #Quad 2
        angle=angle+180
    elif x>0 and y<0: #Quad 4
        angle=angle

    t.lt(angle)
    t.fd(hyp)
    t.lt(360-angle)  
    if line_color != None:
        t.pencolor(lc)  
  
def move(t, x, y):
    print("Move without marking a line to a point X:", x, "over and Y:", y, "up")
    t.pu()
    line(t, x, y)
    t.pd()
 
#-----------------------------Arc---------------------------#

def arc(t, radius, angle=360, rotate=0, line_color=None, fill_color=None):
    radius=float(radius)
    angle=float(angle)
    print("Arc, with Radius Size:", radius, "Angle of Arc:", angle, "and Rotation:", rotate, "with", line_color, "lines and", fill_color, "fill")
    if fill_color != None:
        fc = t.fillcolor()
        t.fillcolor(fill_color)
        t.begin_fill()
    if line_color != None:
        lc = t.pencolor()
        t.pencolor(line_color)
    coor=t.pos() #Needed to prevent turtle from drifting
    t.rt(rotate)
    #---Move Turtle---
    t.pu()
    t.bk(radius)
    t.lt(90)
    t.pd()
    #---Draw Arc---
    arcLength=2*pi*radius*angle/360
    sides=int(arcLength/3)+1
    stepLength=arcLength/sides
    stepAngle=float(angle)/sides
    totalAngle=0
    for side in range(sides):
        t.fd(stepLength)
        t.rt(stepAngle) 
        totalAngle+=stepAngle  
    #---Move Turtle Back---
    t.pu()
    t.rt(90)
    t.setpos(coor)
    t.pd()
    t.lt(totalAngle)
    t.lt(rotate)
    if line_color != None:
        t.pencolor(lc)
    if fill_color != None:
        t.end_fill()
        t.fillcolor(fc) 
