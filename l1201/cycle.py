from turtle import *

t = Turtle()

for x in range(10):
    for i in range(2):
        for j in range(15):
            t.fd(10)
            t.rt(6)
        t.rt(90)
    t.rt(36)

done()