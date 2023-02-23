import time
import pygame
from pygame.locals import *

#define the postion of airplan
hero_x=400
hero_y=500
enemy_x=430
enemy_y=10
ememy_path='right'
#定义子弹仓
my_bullet=[]
#加载爆炸多张图片
a=pygame.image.load('./feiji/enemy2_down1.png')
b=pygame.image.load('./feiji/enemy2_down2.png')
c=pygame.image.load('./feiji/enemy2_down3.png')
d=pygame.image.load('./feiji/enemy2_down4.png')
e=pygame.image.load('./feiji/enemy2_down5.png')
f=pygame.image.load('./feiji/enemy2_down6.png')
blow_up=[a,b,c,d,e,f]
#vaerialble enemy status
enemy_life='life'
#初始值为0 代表加载第一张图片，不能超过6
enemy_number=0

#判断飞机状态


def enemy_plan(screen,enemy):
    global enemy_x
    global enemy_y
    global ememy_path
    global enemy_life
    global enemy_number
    for bullet in my_bullet:
        if (bullet['x'] >= enemy_x+50 and bullet['y'] <= enemy_x + 100 and bullet['y'] >= 0 and bullet['y'] <= 256):
            enemy_life = 'dead'
    if enemy_life == 'life':
        screen.blit(enemy, (enemy_x, enemy_y))
        if enemy_x >= 755:
            ememy_path = 'left'
        elif enemy_x <= 0:
            ememy_path = 'right'
        if ememy_path == 'left':
            enemy_x -= 10
        elif ememy_path == 'right':
            enemy_x += 10
    elif enemy_life=='dead':
        if enemy_number <=5:
            screen.blit(blow_up[enemy_number],(enemy_x,enemy_y))
            enemy_number = enemy_number + 1



def hero_plan(screen,hero,bullet):
    global hero_x
    global hero_y

    screen.blit(hero,(hero_x,hero_y))
    for event in  pygame.event.get(): #return a list []
      if event.type ==QUIT :
          exit()
      if event.type==KEYDOWN:
          if event.key==K_UP:
              hero_y = hero_y-15
          if event.key ==K_DOWN:
              hero_y = hero_y+15
          if event.key ==K_LEFT:
              hero_x = hero_x-15
          if event.key ==K_RIGHT:
              hero_x = hero_x +15
          if event.key == K_SPACE:
              my_bullet.append({'x':hero_x+30,'y':hero_y-20})
    for i in my_bullet:
        screen.blit(bullet,(i['x'],i['y']))
        i['y']-=10





def main():
    screen=pygame.display.set_mode((885,650),0,32)
    background=pygame.image.load('./feiji/back_ground_new.png')
    hero=pygame.image.load('./feiji/hero1.png')
    bullet=pygame.image.load('./feiji/plane.png')
    enemy=pygame.image.load('./feiji/enemy2.png')
    #method blit()for 粘贴图片.blit(横坐标，纵坐标)

    while True:
        screen.blit(background, (0, 0))
        # function for stick and paste the airplan
        hero_plan(screen, hero,bullet)
        enemy_plan(screen,enemy)
        pygame.display.set_caption('spaceship flight')
        pygame.display.update()
        pygame.event.get()
        time.sleep(0.05)

#define the gate for game
if __name__=='__main__':
 main()