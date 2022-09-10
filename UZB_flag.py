

#The National Flag of Uzbekistan


from turtle import *
from math import *


def funk1(x, y, rang):
	tt.pencolor(rang)
	tt.fillcolor(rang)

	tt.penup()
	tt.speed(1*N)
	tt.goto(x, y)
	tt.pendown()
	tt.pensize(n)
	
	tt.begin_fill()
	tt.speed(4*N)
	tt.fd(250*n)
	tt.right(90)
	tt.fd(40*n)
	tt.right(90)
	tt.fd(250*n)
	tt.right(90)
	tt.fd(40*n)
	tt.end_fill()

def funk2(x, y):
	tt.pencolor('red')
	tt.penup()
	tt.speed(1*N)
	tt.goto(x, y)

	tt.pendown()
	
	tt.speed(4*N)
	tt.pensize(2.5*n)
	tt.fd(250*n)

def yulduz(x, y):
	
	tt.penup()
	tt.speed(1*N)
	a = 3*n
	tt.goto(x, y+a)
	tt.pencolor('white')
	tt.fillcolor('white')
	tt.pensize(1)
	tt.pendown()
	tt.begin_fill()
	tt.right(144)
	tt.goto(a*cos(radians(-54))+x, a*sin(radians(-54))+y)
	tt.right(144)
	tt.goto(a*cos(radians(162))+x, a*sin(radians(162))+y)
	tt.right(144)
	tt.goto(a*cos(radians(18))+x, a*sin(radians(18))+y)
	tt.right(144)
	tt.goto(a*cos(radians(234))+x, a*sin(radians(234))+y)
	tt.right(144)
	tt.goto(x, y+a)
	tt.end_fill()
	tt.left(36)


def main():
	global tt, n, N


	while True:
		n = input("O'lchamni kiriting: ")
		N = input("Tezlikni kiriting: ")
		if n.isdigit() and N.isdigit():
			n = float(n)/250
			N = float(N)
			break
		else:
			print("Xatolik. Qayta urinib ko'ring:  ")
			print('')

	oyna = Screen()
	oyna.bgcolor('black')

	tt = Turtle()
	tt.shape('turtle')
	tt.shapesize(1.5, 1.5, 3)
	tt.pencolor('white')
	



	funk1(-125*n, 62.5*n, 'blue')
	tt.right(90)
	funk1(-125*n, 20*n, 'white')
	tt.right(90)
	funk1(-125*n, -22.5*n, 'green')
	tt.right(90)
	funk2(-125*n, 21.25*n)
	funk2(-125*n, -21.5*n)
	for i1 in range(3):
		x, y = -31*n, 30.5*n + i1*12*n
		for i2 in range(5-i1):
			yulduz(x, y)
			x -= 12*n



	tt.penup()
	tt.goto(-90*n, 42.5*n)
	tt.hideturtle()
	tt1 = Turtle()
	tt2 = Turtle()
	tt1.penup()
	tt2.penup()
	tt1.speed(0)
	tt2.speed(0)
	tt1.color('white')
	tt1.goto(-95*n, 42.5*n)	
	
	tt2.goto(-90*n, 42.5*n)
	tt1.shape('circle')
	tt2.shape('circle')
	tt1.shapesize(1.5*n)
	tt2.color('blue')
	tt2.shapesize(1.25*n)

	tt.showturtle()
	tt.right(72)
	tt.goto(600, 0)
	#tt.hideturtle()
	tt3 = Turtle()
	tt3.speed(5)
	tt3.hideturtle()
	tt3.penup()
	tt3.goto(-127*n, 64.5*n)
	tt3.pendown()
	tt3.pensize(4.5*n)
	tt3.goto(127*n, 64.5*n)
	tt3.goto(127*n, -64.5*n)
	tt3.goto(-127*n, -64.5*n)
	tt3.goto(-127*n, 64.5*n)
	tt.hideturtle()
	oyna.mainloop()
	input()
main()
