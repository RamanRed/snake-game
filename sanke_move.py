from turtle import Screen, Turtle
from random import *

class sankeMove:
        HighScore=0
        src=Screen()    
# Creating a Sanke ____________________________________________________________________________________________________    
        sanke_obj=[] 
        head=None

        def __init__(self):
            
            for i in range(3):
                t1=Turtle(shape="square")                
                t1.resizemode("user")
                t1.shapesize(5/4,5/4)
                t1.goto((-i)*10,0)
                t1.color("gray")
                t1.penup()
                self.sanke_obj.append(t1)
            self.head=self.sanke_obj[0] 
            
            
#Resetting the Game________________________________________________________________________________________________________________________________________________________________
        
        def reset(self):
            for i in self.sanke_obj:
                #i.clear() won't  do anything 
                i.goto(1000,1000)
            self.sanke_obj=[]
            self.__init__()    
                    
# Adding Sanke________________________________________________________________

        def pluse(self):
            #n=len(self.sanke_obj)
            #    hh=self.head.heading()
            for i in range(0, len(self.sanke_obj)):
                if i != 0:
                    x=self.sanke_obj[i].xcor()
                    y=self.sanke_obj[i].ycor()
                    self.sanke_obj[i].goto(x1,y1)
                    x1=x
                    y1=y 
                if i==0:
                    x1=self.sanke_obj[i].xcor()
                    y1=self.sanke_obj[i].ycor()
                    self.sanke_obj[i].forward(20)    
            t1=Turtle(shape="square")                
            t1.resizemode("user")
            t1.shapesize(5/4,5/4)
            t1.goto(x1,y1)
            t1.color("gray")
            t1.penup()
            self.sanke_obj.append(t1)        
         
# snake MOvements-----------------------------------------------------------------------------------------------------     
        def move(self):
            
            for i in range(0, len(self.sanke_obj)):
                if i != 0:
                    x=self.sanke_obj[i].xcor()
                    y=self.sanke_obj[i].ycor()
                    self.sanke_obj[i].goto(x1,y1)
                    x1=x
                    y1=y 
                if i==0:
                    x1=self.sanke_obj[i].xcor()
                    y1=self.sanke_obj[i].ycor()
                    self.sanke_obj[i].forward(20)    
        
            self.src.update()
            
        def move_u(self):
            
            if self.head.heading() != 270:
                self.head.setheading(90)    
            
        def move_d(self):
            
            if self.head.heading() != 90:
                self.head.setheading(270)
            
        def move_l(self):
            
            if self.head.heading() != 0 :
                self.head.setheading(180)
            
        def move_r(self):
            
            if self.head.heading() != 180:
                self.head.setheading(0)
                
# food item_______________________________________________________________________________________________________________________________________

class food(Turtle):
    
    def __init__(self):
        super().__init__()
        
    def ran_food(self, tlist):
        cord=[]
        for i in tlist:
             
             a=i.xcor()
             b=i.ycor()
             xy=(a,b)               
             cord.append(xy)
             
        c=True
        while c:
            x=randint(-340,340)   
            y=randint(-340,340)
            pq=(x,y)
            
            if pq not in cord:
                c=False
        
                
        self.shape("circle")
        self.shapesize(5/4, 5/4)
        self.color("red")
        p=Screen()
        p.update()
        self.penup()
        self.goto(pq[0],pq[1])
    
    def eat(self, a2 ,a1):
         if a2.distance(a1) <= 20:
             return 1    

# scoreboard_______________________________________________________________________________________________________________________________________________________________

class scoreb(Turtle):

    t=Turtle()
    
    def __init__(self):
        super().__init__()
    
    def scor(self,s):
        self.clear()
        self.penup()
        self.hideturtle()
        self.write(f"Score{s}", align="center", font=("Arial", 20, "normal"))    
        self.goto(100,360)
        self.color("white")


    def HS(self, hs):
        self.t.clear()
        self.t.penup()
        self.t.hideturtle()
        self.t.write(f"HighScore{hs}", align="center", font=("Arial", 20, "normal"))    
        self.t.goto(-100,360)
        self.t.color("white")

# GameOver______________________________________________________________________________________________________________________________________________________________________

def GameOver():
    p=Turtle()
    p.hideturtle()
    p.color("#000000")
    p.write(f"Game OVER", align="center", font=("Arial", 24, "normal"))                               
                              
                 
#check_tail________________________________________________________________________________________________________________________________________________________________

def check( tlist):
        for i in tlist[3:]:
               if tlist[0].distance(i) <=20 :
                   GameOver()
                   return 1
               
            
                    

