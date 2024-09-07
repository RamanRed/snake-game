from turtle import Screen
from time import sleep
from sanke_move import  sankeMove, food, scoreb, check, GameOver

src=Screen()
src.bgcolor("black")
src.title(" My Game ")
src.setup(720,820)
src.tracer(0) 
src.listen()
san=sankeMove()
foo=food()
score=0
sd=scoreb()
foo.ran_food(san.sanke_obj)


while True:
    
    with open("highScore.txt", mode="r") as fil:
        hscore=fil.read(4)
        san.HighScore=hscore
    
    
    sd.scor(score)
    sd.HS(san.HighScore)    
    
    
    san.move()
    w=0
    w=foo.eat(foo, san.sanke_obj[0])
    if w==1:
        score=score+1
        san.pluse()
        foo.ran_food(san.sanke_obj)
        w=0
        
    sleep(0.1)
    j=check(san.sanke_obj)
    
    if j==1:
        break
    
    src.onkey(san.move_u, key="Up")    
    src.onkey(san.move_d, key="Down")    
    src.onkey(san.move_l, key="Left")    
    src.onkey(san.move_r, key="Right")  
    src.onkey(san.pluse, key="p")
    if san.sanke_obj[0].xcor() >= 360 or  san.sanke_obj[0].ycor() >= 360 or san.sanke_obj[0].xcor() <= -360 or  san.sanke_obj[0].ycor() <= -360:
        san.reset()
        
        if score> int(san.HighScore):
                san.HighScore=score
                file=open("highScore.txt", mode="w")
                file.write(str(san.HighScore))    
                file.close()
        src.clear()
        GameOver()  
        break
          
src.exitonclick()