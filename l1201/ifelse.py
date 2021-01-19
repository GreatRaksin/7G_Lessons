from turtle import *

t = Turtle()

n = int(input('Введите число: '))
if n <= 10:
    t.color('red')
    t.dot(50)
else:
    t.color('green')
    t.dot(50)

done()