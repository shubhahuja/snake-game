import random
import sys
import pygame
from pygame.locals import *
pygame.init() #initializing pygame
pygame.display.set_caption("snake game")
#Global Variables
rows = 10
width = 500
height = 500
w = 500
MARGIN = 0
surface = pygame.display.set_mode((500, 600))
score =0
BLACK = (0,0,0)
GREEN = (0,255,0)
RED = (255,0,0)
WHITE = (255,255,255)
game_status=True

def drawGrid():
    MARGIN = w // rows

    x = 0
    y = 0
    for l in range(rows):
        x = x + MARGIN
        y = y + MARGIN

        pygame.draw.line(surface, WHITE, (x,0),(x,w))
        pygame.draw.line(surface, WHITE, (0,y),(w,y))

class Snakes():
    def __init__(self,master,sur):
        self.x=0
        self.y=0
        self.snakelist=[master]
        self.surf=sur
        self.master_snake=master


    def update_master(self,master):
        self.master_snake=master


    def add_snake(self,s):

       
        self.snakelist.append(s)


    def update_snakes(self,master):

            for i in range(-1,-len(self.snakelist),-1):
                self.snakelist[i].update_cord_to(self.snakelist[i-1].x,self.snakelist[i-1].y)
                self.snakelist[i].update_dir(self.snakelist[i-1].direction)
        

        
       

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.surf = pygame.Surface((50,50))
        self.surf.fill(GREEN)
        self.x=0
        self.y=0
        self.size=50
        self.direction="U"  # directions = U , D , R , L
    def update_cord(self,x1,y1):
        self.x+=x1
        self.y+=y1
        if self.x<0 :
            self.x=450
        elif self.x>450:
            self.x=0
        if self.y<0 :
            self.y=450
        elif self.y>450:
            self.y=0
    def update_cord_to(self,x1,y1):
        self.x=x1
        self.y=y1

    def update_dir(self,d):
        self.direction=d

class Fruit():
    def __init__(self):
        
        self.x=random.randint(0,9)*50
        self.y=random.randint(0,9)*50
        self.size=50
        self.status=False
    def create_fruit(self):
        self.status=False
        self.x=random.randint(0,9)*50
        self.y=random.randint(0,9)*50

   
snake=Player()
fruit=Fruit()
the_snake=Snakes(snake,surface) 

def update_cord_gen(s):
    if s.direction=="U":
        x1=0
        y1=-50
    elif s.direction=="D":
        x1=0
        y1=50
    elif s.direction=="R":
        x1=50
        y1=0
    elif s.direction=="L":
        x1=-50
        y1=0
    return [x1,y1]   
text='COME ON'

while game_status:

    clock = pygame.time.Clock()
    
    for event in pygame.event.get():
        x1=0
        y1=0
        direction=snake.direction
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            pygame.quit()
            sys.exit()
    
        elif event.type == KEYDOWN and event.key== K_UP:
            if snake.direction=="D":
                direction="D"
            else:
                direction="U"
        elif event.type == KEYDOWN and event.key== K_DOWN:
            if snake.direction=="U":
                direction="U"    
            else:
                direction="D"
        elif event.type == KEYDOWN and event.key== K_RIGHT:
            if snake.direction=="L":
                direction="L"
            else:
                direction="R"
        elif event.type == KEYDOWN and event.key== K_LEFT:
            if snake.direction=="R":
                direction="R"
            else:
                direction="L"  

    snake.update_dir(direction)


    if snake.direction=="U":
        x1=0
        y1=-50
    elif snake.direction=="D":
        x1=0
        y1=50
    elif snake.direction=="R":
        x1=50
        y1=0
    elif snake.direction=="L":
        x1=-50
        y1=0   
  
    ##snake.update_cord(x1,y1)
    the_snake.update_snakes(snake)
    the_snake.update_master(snake)
    snake.update_cord(x1,y1)
    ##the_snake.update_snakes(snake)
    print(len(the_snake.snakelist))


    if snake.x==fruit.x and snake.y==fruit.y:
        fruit.status=True
        score=score+10
        a=random.randint(0,6)
        l=["YAY!","WOW ! ", "KEEP GOING", "AMAZING!" , "YUMM!" , "DAMNN!! ;)" ,"TASTY!"]
        text=l[a]


        
    if fruit.status:
        s=Player()
        s.update_cord_to(fruit.x+x1,fruit.y+y1)
        
        the_snake.add_snake(s)
        fruit.create_fruit()
    
    for i in the_snake.snakelist[1:]:
        if i.x==snake.x and i.y==snake.y:
            text="GAME OVER"
            game_status=False

    

    
    surface.fill((0, 0, 0))  # Fills the screen with black
    drawGrid()  # Will draw our grid lines

    pygame.draw.rect(surface,GREEN,[snake.x, snake.y ,snake.size,snake.size ])
 ##   pygame.draw.rect(surface,RED,[fruit.x,fruit.y,50,50])
    for i in range(len(the_snake.snakelist)):
        if i==0:
            pygame.draw.rect(surface,(255,255,0),[the_snake.snakelist[i].x, the_snake.snakelist[i].y ,snake.size,snake.size ]) 

        else:
            pygame.draw.rect(surface,GREEN,[the_snake.snakelist[i].x, the_snake.snakelist[i].y ,snake.size,snake.size ]) 
    pygame.draw.rect(surface,RED,[fruit.x,fruit.y,50,50])
    pygame.font.init() 
    myfont = pygame.font.SysFont('Comic Sans MS', 30)
    textsurface = myfont.render('Score : '+ str(score), False,  (0,255,255))

    textsurface2 = myfont.render(text, False,  (0,255,255))

    surface.blit(textsurface,(160,500))
    surface.blit(textsurface2,(130,550))
    pygame.display.update()
    clock.tick(10)
    
    
pygame.font.init() 
myfont = pygame.font.SysFont('Comic Sans MS', 70)
textsurface = myfont.render('Score : '+ str(score), False,  (0,255,255))

textsurface2 = myfont.render('GAME over!!', False,  (0,255,255))

surface.blit(textsurface,(160,200))
surface.blit(textsurface2,(130,400))
pygame.display.update()
            





