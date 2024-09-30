# ----Setup-----
from turtle import *
bob = Turtle() #Name your turtle

# ----Code-----

bob.speed(0)


def square(size):
    count = 0;
    while count < 4:
      bob.fd(size)
      bob.lt(90)
      count = count + 1
      print(count)

def star(size):
     count = 0;
        while count <5:
        bob.fd(80)
        bob.rt(144)
        count = count +1
        print(count)


done()
