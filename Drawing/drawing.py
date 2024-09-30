from shapes_new import *

def house (t, size = 10, color=None):
  square(t, size*6, 0, None, color)
  
  move(t, size*0, size*6)
  roof(t, size)
  move(t, size*0, size*-6)
  door(t, size*3)
  move(t, size*4, size*3)
  window(t, size*1)

def door(t, size =10, color=None):
  rect(t, size*.5, size*1, 0, None, "pink")
  move(t, .4*size, .5*size)
  arc(t, size*.08, 360, 0, None, "yellow")
  move(t, -.24*size, .2*size)
  window(t, size*.1, "blue")
  move(t, -.16*size, -.7*size)
  
def roof(t, size=10):
    sss_tri(t, size*6, size*4, size*4, 0, None, "green")
    
    move(t, 3*size, 1*size)
    dormir(t, size*1)
    move(t, -3*size, -1*size)
    
    
def window(t, size=10, color="white"):
    count = 0
    while count < 4:
        square(t, size*1, 0, None, color)
        t.lt(90)
        count+=1

def dormir(t, size=10, color="blue"):
    arc(t, size*1, 360, 0, None, color)
    count = 0
    while count < 4:
        t.lt(90)
        t.fd(size*1)
        t.bk(size*1)
        count +=1
