

#   Captain America Shield



from turtle import Turtle, Screen
from math import *
from random import *




def kordinata():
	global kx, ky
	kx = randint(-400, 400)
	ky = randint(-300, 300)
	if kx**2 + ky**2 <= 150**2:
		kordinata()


# def nuqta():
# 	nuq = Turtle()
# 	nuq.color(ranglar[randint(0,8)])
	
# 	nuq.shape('circle')
# 	nuq.speed(0)
# 	nuq.shapesize(0.05)
	
# 	nuq.penup()
# 	kordinata()
# 	nuq.goto(kx, ky)

	
def aylana(a, b):
	top = Turtle()
	top.shape('circle')
	top.shapesize(a)
	top.color(b)
	top.goto(0, 0)



def yulduz(a):
	global q
	yul = Turtle()
	
	yul.pencolor('white')
	yul.fillcolor('white')
	yul.hideturtle()
	yul.penup()
	yul.speed(0)
	
	
	yul.goto(0, a)
	yul.begin_fill()
	yul.pendown()
	yul.goto(a*cos(radians(-54)), a*sin(radians(-54)))
	yul.goto(a*cos(radians(162)), a*sin(radians(162)))
	yul.goto(a*cos(radians(18)), a*sin(radians(18)))
	yul.goto(a*cos(radians(234)), a*sin(radians(234)))
	yul.goto(0, a)
	yul.end_fill()

def main():
	global q, ranglar
	oyna = Screen()
	oyna.bgcolor('black')
	ranglar=['yellow','green', 'black', 'grey', 'orange', 'white', 'brown', 'pink', 'magenta']

	aylana(15, 'red')
	aylana(12, 'white')
	aylana(9, 'red')
	aylana(6, 'blue')
	
	a = 60
	yulduz(a)

	# for i in range(1000):
	# 	nuqta()
						
	oyna.mainloop()

main()	