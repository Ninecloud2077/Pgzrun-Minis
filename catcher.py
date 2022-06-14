import pgzrun
from random import randint

WIDTH=HEIGHT=500

b=Actor('circle',(WIDTH//2,HEIGHT//2))

win=0
times=0

def move():
    global b
    b.center=(randint(50,WIDTH-b.width//2),randint(50,HEIGHT-b.height//2))
    
def draw():
    global win,times
    screen.fill((255,255,255))
    b.draw()
    if win:
        if times<=30:
            screen.draw.text('Unbeliveable!',(100,100),fontsize=90,color='yellow')
        elif times<=75:
            screen.draw.text('Awesome!',(100,100),fontsize=100,color='yellow')
        elif times<=100:
            screen.draw.text('Sucsess!',(100,100),fontsize=100,color='yellow')
        elif times<150:
            screen.draw.text('Good Job!',(100,100),fontsize=100,color='yellow')
        else:
            screen.draw.text('Loser!',(100,100),fontsize=100,color='black')
        screen.draw.text('Score:'+str(times),(100,180),fontsize=40,color='black')
    else:
        screen.draw.text(str(times),(15,15),fontsize=45,color='black')
        
def on_mouse_move(pos):
    if (not win) and b.distance_to(pos)<=80:
        move()
        
def on_mouse_down(pos,button):
    global win,times
    if button==mouse.LEFT:
        if b.distance_to(pos)<=70:
            win=1
            clock.unschedule(move)
        else:
            times+=1
            if times>=150:
                win=1
                clock.unschedule(move)
    
clock.schedule_interval(move,1.5)

pgzrun.go()
