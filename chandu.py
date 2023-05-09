import pygame
from pygame import mixer
import random
import time
def my_game():
    from heartgame import final_game
    pygame.init()
    mixer.init()
    mixer.music.load("digital-love-127441.mp3")
    mixer.music.set_volume(0.4)
    mixer.music.play(loops=-1)
    size = [360,720]
    green =(0,225,0)
    font = pygame.font.SysFont("Comic sans MS",20)
    screen = pygame.display.set_mode(size)
    background = pygame.image.load("kelly.jpg")
    obj = pygame.image.load("object.png")
    me = pygame.image.load("user0.png")
    f2 = pygame.font.SysFont("Comic sans MS",50)
    text = font.render("No Lifes-Score:",True,green)
    over = f2.render("Game Over!",True,(225,0,0))
    win = f2.render("You Win!", True, (225, 0, 0))
    global x,y
    x,y = 0,0
    def num():
        global x,y,z
        x += 0.01
        if str(x)[3]=="0":
            y +=1
            x=0
            count = font.render(str(int(y)),True,green)
            screen.blit(count,[280,0])
            if y % 10 == 0:
                z += 0.20


    def rand():
        return -1*random.randint(0,800)

    obj_y = [rand(),rand(),rand(),rand()]
    global z
    z =5
    def update(i):
        global y,z
        obj_y[i] += z
        if obj_y[i]>580:
            obj_y[i]=rand()
    clock = pygame.time.Clock()
    userx=0
    while True:
        pygame.event.get()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT] and userx<220:
            userx += 10
        elif keys[pygame.K_LEFT] and userx>-100:
            userx -= 10

        update(0)
        update(1)
        update(2)
        update(3)
        screen.blit(background,[0,0])
        screen.blit(text,[120,0])
        screen.blit(me,[userx,200])
        screen.blit(obj,[-60,obj_y[0]])
        screen.blit(obj,[30,obj_y[1]])
        screen.blit(obj,[125,obj_y[2]])
        screen.blit(obj,[220,obj_y[3]])
        num()
        if z>=20:
            screen.blit(win,[40, 310])
            if z>=20.20:
                time.sleep(1)
                final_game(y)
        else:
            if obj_y[0]>450 and userx <=-25:
                print("Game Over")
                screen.blit(over, [40, 310])
                if obj_y[0]>470:
                    time.sleep(2)
                    final_game(y)
            elif obj_y[1]>450 and (userx <=45 and userx>=-45):
                print("Game Over")
                screen.blit(over, [40, 310])
                if obj_y[1] > 470:
                    time.sleep(2)
                    final_game(y)
            elif obj_y[2]>450 and (userx <=145 and userx>=55):
                print("Game Over")
                screen.blit(over, [40, 310])
                if obj_y[2] > 470:
                    time.sleep(2)
                    final_game(y)
            elif obj_y[3]>450 and userx >=150:
                print("Game Over")
                screen.blit(over, [40, 310])
                if obj_y[3] > 470:
                    time.sleep(2)
                    final_game(y)
        pygame.display.update()
        clock.tick(20)

