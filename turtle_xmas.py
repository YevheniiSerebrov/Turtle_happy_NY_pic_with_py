import turtle
import random

#***************************Colors*********************************
colors=["red","blue","white","#991371","orange"]

#******************rectangle*******************
def rectangle(size_x,size_y, pos_x=0, pos_y=0,color="grey"):
    joe=turtle.Turtle()
    joe.hideturtle()
    joe.begin_fill()
    joe.color(color)
    joe.up()
    joe.setposition(pos_x,pos_y)
    joe.down()
    joe.forward(size_x/2)
    joe.left(90)
    joe.forward(size_y)
    joe.left(90)
    joe.forward(size_x)
    joe.left(90)
    joe.forward(size_y)
    joe.left(90)
    joe.forward(size_x/2)
    joe.end_fill()
 
# ********************circle*******************************
def circle(radius,pos_x=0, pos_y=0, color="#B1C1F1"):
    joe=turtle.Turtle()
    joe.speed(10)
    joe.hideturtle()
    joe.up()
    joe.setposition(pos_x,pos_y)
    joe.down()
    joe.begin_fill()
    joe.color(color)
    h=2*3.14159*radius/15
    for a in range(15):
        joe.forward(h)
        joe.right(24)
    joe.end_fill()

# ********************ellipse*******************************
def elipse(radius,angle=-45,pos_x=0, pos_y=0, color="#B1C1F1"):
    joe=turtle.Turtle()
    joe.hideturtle()
    joe.up()
    joe.setposition(pos_x,pos_y)
    joe.down()
    joe.begin_fill()
    joe.color(color)
    joe.seth(angle)
    for i in range(2):
        joe.circle(radius,90)
        joe.circle(radius//2, 90)
    joe.end_fill()

# # ********************star*******************************
def star(size, angle=0, pos_x=0, pos_y=0, color="yellow"):
    joe=turtle.Turtle()
    joe.hideturtle()
    joe.begin_fill()
    joe.color(color)
    joe.up()
    joe.setposition(pos_x,pos_y)
    joe.down()
    for i in range(5):
        joe.right(angle)
        joe.forward(size)
        angle=5//2*360/5
    joe.end_fill()
# star(50, angle=60, pos_x=50, pos_y=-100, color="black")
# star(10, angle=20, pos_x=100, pos_y=-100, color="blue")
# star(20, pos_x=200, pos_y=-100, color="pink")

#**************************square****************************
def square(size, pos_x=0,pos_y=0,color="orange"):
    joe=turtle.Turtle()
    joe.speed(0)
    joe.hideturtle()
    joe.begin_fill()
    joe.color(color)
    joe.up()
    joe.setposition(pos_x,pos_y)
    joe.down()
    for i in range(4):
        joe.forward(size)
        joe.left(90)
    joe.end_fill()
#**************************Semicircle****************************
def semicircle(size,angle=0, pos_x=0,pos_y=0,color="white"):
    joe=turtle.Turtle()
    joe.speed(0)
    joe.hideturtle()
    joe.begin_fill()
    joe.color(color)
    joe.up()
    joe.setposition(pos_x,pos_y)
    joe.down()
    joe.right(angle)
    joe.circle(size,180)
    joe.left(90)
    joe.forward(2*size)
    
    # for i in range(31):
    #     joe.forward(6)
    #     joe.left(6)
    # joe.left(92)
    # joe.forward(0.1*size)
    joe.end_fill()

#**************************triangle***************************
def triangle(size, pos_x=0,pos_y=0,color = "#105409"):
    joe=turtle.Turtle()
    joe.hideturtle()
    joe.speed(100)
    joe.up()
    joe.setposition(pos_x,pos_y)
    joe.down()
    joe.begin_fill()
    joe.color(color)
    joe.forward(size/2)
    joe.left(120)
    joe.forward(size)
    joe.left(120)
    joe.forward(size)
    joe.left(120)
    joe.forward(size/2)
    joe.end_fill()

# ***************************Trees*********************************
def xmas_tree(size, pos_xx, pos_yy, color_tree):
    triangle(size, pos_xx, pos_y=pos_yy, color=color_tree)
    triangle(size*0.9,pos_xx,pos_y=pos_yy+size*0.2,color=color_tree )
    triangle(size*0.8,pos_xx,pos_y=pos_yy+size*0.4,color=color_tree)
    triangle(size*0.7,pos_xx,pos_y=pos_yy+size*0.6,color=color_tree)
    triangle(size*0.6,pos_xx,pos_y=pos_yy+size*0.8,color=color_tree)
    rectangle(size/5,size/6, pos_x=pos_xx,pos_y=pos_yy-(size/6), color="brown")
    for i in range(1,5):
            circle(0.03*size, pos_xx, pos_yy+size*0.3*i, color=random.choice(colors))  
            circle(0.04*size, pos_xx-size*0.15, pos_yy+size*0.23*i, color=random.choice(colors))
            circle(0.03*size, pos_xx+size*0.15, pos_yy+size*0.23*i, color=random.choice(colors))
            circle(0.02*size, pos_xx-size*0.24, pos_yy+size*0.23*i, color=random.choice(colors))
            circle(0.03*size, pos_xx+size*0.26, pos_yy+size*0.23*i, color=random.choice(colors))

# ***************************Houses*********************************
def city_houses(size_height, pos_xx=0, pos_yy=0):
    rectangle(50,size_height*0.9, pos_x=pos_xx, pos_y=pos_yy,color="#262325")

    semicircle(10,angle=90, pos_x=pos_xx-10,pos_y=pos_yy+20)

    square(7,pos_x=pos_xx-20,pos_y=pos_yy+size_height-30)
    square(7,pos_x=pos_xx-5,pos_y=pos_yy+size_height-30)
    square(7,pos_x=pos_xx+10,pos_y=pos_yy+size_height-30)

    square(7,pos_x=pos_xx-20,pos_y=pos_yy+size_height-60)
    square(7,pos_x=pos_xx-5,pos_y=pos_yy+size_height-60)
    square(7,pos_x=pos_xx+10,pos_y=pos_yy+size_height-60)

    rectangle(50,size_height*0.8, pos_x=pos_xx+50, pos_y=pos_yy,color="#202020")
    square(7,pos_x=pos_xx+30,pos_y=pos_yy+size_height*0.8-30)
    square(7,pos_x=pos_xx+45,pos_y=pos_yy+size_height*0.8-30)
    square(7,pos_x=pos_xx+60,pos_y=pos_yy+size_height*0.8-30)

    square(7,pos_x=pos_xx+30,pos_y=pos_yy+size_height*0.8-60)
    square(7,pos_x=pos_xx+45,pos_y=pos_yy+size_height*0.8-60)
    square(7,pos_x=pos_xx+60,pos_y=pos_yy+size_height*0.8-60)

    rectangle(50,size_height*1.3, pos_x=pos_xx+100, pos_y=pos_yy,color="#262325")
    square(7,pos_x=pos_xx+80,pos_y=pos_yy+size_height-10)
    square(7,pos_x=pos_xx+110,pos_y=pos_yy+size_height-10)
    semicircle(10,angle=90, pos_x=pos_xx+87,pos_y=pos_yy+25)
  
    rectangle(50,size_height*1.1, pos_x=pos_xx+150, pos_y=pos_yy,color="#131313")
    square(7,pos_x=pos_xx+130,pos_y=pos_yy+size_height-30)
    square(7,pos_x=pos_xx+145,pos_y=pos_yy+size_height-30)
    square(7,pos_x=pos_xx+160,pos_y=pos_yy+size_height-30)

    square(7,pos_x=pos_xx+130,pos_y=pos_yy+size_height-60)
    square(7,pos_x=pos_xx+145,pos_y=pos_yy+size_height-60)
    square(7,pos_x=pos_xx+160,pos_y=pos_yy+size_height-60)

    rectangle(50,size_height*0.8, pos_x=pos_xx+200, pos_y=pos_yy,color="#202020")
    square(7,pos_x=pos_xx+180,pos_y=pos_yy+size_height*0.8-30)
    square(7,pos_x=pos_xx+195,pos_y=pos_yy+size_height*0.8-30)
    square(7,pos_x=pos_xx+210,pos_y=pos_yy+size_height*0.8-30)

    square(7,pos_x=pos_xx+180,pos_y=pos_yy+size_height*0.8-60)
    square(7,pos_x=pos_xx+195,pos_y=pos_yy+size_height*0.8-60)
    square(7,pos_x=pos_xx+210,pos_y=pos_yy+size_height*0.8-60)
#************************houses_shadows******************************************
def shad_houses(size_height, pos_xx=0, pos_yy=0):
    rectangle(50,size_height*0.8, pos_x=pos_xx+50, pos_y=pos_yy,color="black")
    rectangle(50,size_height*1.3, pos_x=pos_xx+100, pos_y=pos_yy,color="black")
    rectangle(50,size_height*0.9, pos_x=pos_xx, pos_y=pos_yy,color="black")

    rectangle(50,size_height*1.1, pos_x=pos_xx+150, pos_y=pos_yy,color="black")
    rectangle(50,size_height*0.8, pos_x=pos_xx+200, pos_y=pos_yy,color="black")
# ***********************kite*********************************
def kite(size,angle=0, pos_x=10, pos_y=50,color="grey"):
    joe=turtle.Turtle()
    joe.hideturtle()
    joe.up()
    joe.setposition(pos_x,pos_y)
    joe.down()
    joe.begin_fill()
    joe.color(color)
    joe.left(angle+60)
    joe.forward(size)
    joe.left(75)
    joe.forward(size/1.4142)
    joe.left(90)
    joe.forward(size/1.4142)
    joe.left(75)
    joe.forward(size)
    joe.left(150)
    joe.forward(size*1.3625)
    
    joe.end_fill()
# *****************************curve********************************
def curve(size, pos_x=0,pos_y=0,color="black"):
    joe=turtle.Turtle()
    joe.speed(0)
    joe.hideturtle()
    joe.color(color)
    joe.up()
    joe.setposition(pos_x,pos_y)
    joe.down()
    for i in range(5):
        joe.right(60)
        joe.forward(size)
        joe.left(60)
        joe.forward(size)
#************************Tape***********************************************
def tape(size, pos_x=0,pos_y=0,color="#602560"):
    joe=turtle.Turtle()
    joe.speed(0)
    joe.hideturtle()
    joe.up()
    joe.setposition(pos_x,pos_y)
    joe.down()
    joe.begin_fill()
    joe.color(color)

    joe.forward(size)
    joe.left(40)
    joe.forward(size)
    joe.left(140)
    joe.forward(size)
    joe.left(40)
    joe.forward(size)
    joe.right(80)
    joe.forward(size)
    joe.left(40)
    joe.forward(size)
    joe.left(140)
    joe.forward(size)
    joe.left(40)
    joe.forward(size)
    joe.end_fill()
# *********************************Box********************************
def box(size, pos_xx=0,pos_yy=0,color="#602560"):
    joe=turtle.Turtle()
    joe.speed(0)
    joe.hideturtle()
    square(5*size, pos_x=pos_xx-2*size, pos_y=pos_yy)
    joe.begin_fill()
    joe.color(color)
    joe.up()
    joe.setposition(pos_xx,pos_yy)
    joe.down()
  
    for i in range(4):
        joe.forward(size)
        joe.left(90)
        joe.forward(size*2)
        joe.right(90)
        joe.forward(size*2)
        joe.left(90)
    tape(1.5*size,pos_x=pos_xx+0.5*size, pos_y=pos_yy+5*size)
    joe.end_fill()


#********************************Carrot****************************************
def carrot(size, pos_x=0,pos_y=0,color="#ba3d20"):
    joe=turtle.Turtle()
    joe.speed(0)
    joe.hideturtle()
    joe.up()
    joe.setposition(pos_x,pos_y)
    joe.down()
    joe.begin_fill()
    joe.color(color)

    joe.left(5)
    joe.forward(size)
    joe.left(170)
    joe.forward(size)
    joe.left(95)
    joe.forward(size/5)
    joe.end_fill()

#************************trapez_bin********************************
def trapez(size, pos_x=0,pos_y=0,color="#202060"):
    joe=turtle.Turtle()
    joe.speed(0)
    joe.hideturtle()
    joe.up()
    joe.setposition(pos_x,pos_y)
    joe.down()
    joe.begin_fill()
    joe.color(color)

    joe.forward(size)
    joe.left(100)
    joe.forward(1.5*size)
    joe.left(80)
    joe.forward(size/2)
    joe.left(80)
    joe.forward(1.5*size)
    joe.end_fill()

#******************************Snowman***********************************
def snowman(size=1,pos_x=0,pos_y=0):
    c="#8ca4c7"
    circle(size*30, pos_x, pos_y, color=c)
    circle(size*50, pos_x-5*size, pos_y-50*size, color=c)
    circle(size*60, pos_x-7*size, pos_y-120*size, color=c)

    #eyes
    circle(size*3,pos_x-5*size, pos_y-17*size, color="black")
    circle(size*3,pos_x+15*size, pos_y-17*size, color="black")
    carrot(size*50,pos_x+5*size,pos_y-35*size)

    trapez(size*40, pos_x-15*size, pos_y-5*size)
    semicircle(size*10, 90, pos_x-2*size, pos_y-40*size, color="#353535")

    circle(3*size,pos_x+5*size, pos_y-65*size, color="black")
    circle(3*size,pos_x+5*size, pos_y-80*size, color="#451515")
    circle(3*size,pos_x+5*size, pos_y-95*size, color="black")
    circle(3*size,pos_x+5*size, pos_y-110*size, color="#451515")

    circle(4*size,pos_x+5*size, pos_y-150*size, color="black")
    circle(4*size,pos_x+5*size, pos_y-165*size, color="#451515")
    circle(4*size,pos_x+5*size, pos_y-180*size, color="black")
    circle(4*size,pos_x+5*size, pos_y-195*size, color="#451515")



# **********************PICTURE*******************************************
joe=turtle.Turtle()
window=turtle.Screen()
window.tracer(2)
window.bgcolor("#071531")
window.setup(800,500)
#**********************bg**********************************************
rectangle(800,320,pos_y=-250,color="#447699")
rectangle(800,25,pos_y=50,color="#757ca3")
rectangle(800,25,pos_y=25,color="#5c72d0")
rectangle(800,25,pos_y=0,color="#4c6bcb")
rectangle(800,25,pos_y=-25,color="#5c72d0")
rectangle(800,25,pos_y=-50,color="#4d6bcb")
rectangle(800,25,pos_y=-75,color="#757ca3")
rectangle(800,25,pos_y=-100,color="#4d6bcb")
rectangle(800,25,pos_y=-125,color="#5c72d0")
rectangle(800,25,pos_y=-150,color="#4d6bcb")
rectangle(800,25,pos_y=-175,color="#5c72d0")
rectangle(800,25,pos_y=-200,color="#4d6bcb")
rectangle(800,25,pos_y=-225,color="#757ca3")

xmas_tree(100,70,-50, color_tree="#043927") 
xmas_tree(120,-55,-50, color_tree="#234f1e")
xmas_tree(150, 10, -140, color_tree="#0b6623") 

box(10,120, -120, color="red")
box(12,176,-110, color="#501212")
box(7,228, -120, color="green")
box(12,275,-110, color="blue")
box(7,330, -115)
box(12,170,-190, color="#761070")
box(12,270,-200, color="white")
# moon
circle(50,pos_x=300,pos_y=180, color="yellow")
circle(40,pos_x=280,pos_y=180, color="#071531")

star(7,pos_x=270,pos_y=210) 
star(15,pos_x=240,pos_y=180) 
star(9,pos_x=270,pos_y=150) 
star(10,pos_x=-350,pos_y=225) 
star(8,pos_x=-300,pos_y=240) 
star(12,pos_x=-250,pos_y=230) 
star(15,pos_x=-150,pos_y=230) 
star(10,pos_x=-50,pos_y=190) 
star(7,pos_x=0,pos_y=160) 
star(12,pos_x=80,pos_y=200) 
star(8,pos_x=140,pos_y=190) 
star(10,pos_x=210,pos_y=175) 
star(9,pos_x=-280,pos_y=160) 
star(10,pos_x=300,pos_y=230) 
star(9,pos_x=350,pos_y=180)
star(12,pos_x=95,pos_y=150) 
star(8,pos_x=120,pos_y=230) 
star(10,pos_x=30,pos_y=175) 
star(9,pos_x=-240,pos_y=200) 
star(15,pos_x=320,pos_y=200) 
star(9,pos_x=0,pos_y=230)

shad_houses(size_height=120,pos_xx=-340,pos_yy=50)
city_houses(size_height=120,pos_xx=-320,pos_yy=30)

kite(70,angle=20,pos_x=180,pos_y=50, color="#954171")
curve(30,pos_x=180,pos_y=50)
semicircle(10,angle=70, pos_x=160,pos_y=80)
snowman(size=1, pos_x=-200,pos_y= 0)
snowman(size=0.6, pos_x=-300,pos_y= -90)
joe.penup()
joe.setpos(140,220)
joe.color("white")
joe.write("Yevhenii Serebrov ZZIAS1-1111", font=("Century", 13 ))
import time
time.sleep(10)
