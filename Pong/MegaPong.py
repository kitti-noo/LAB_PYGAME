# Megapong.py

import pygame, random
from pygame.locals import *
from pygame.font import *

# some colors
BLACK = (   0,   0,   0)
WHITE = ( 255, 255, 255)
RED   = ( 255,   0,   0)
GREEN = (   0, 255,   0)
BLUE  = ( 0,   0,   255)

WALL_SIZE = 10
STEP = 8

PADDLE_STEP = 10
LEFT  = 0
RIGHT = 1


#(1.2) make the winning score higher from a score of 5 to 10
WINNING_SCORE = 10

class BlockSprite(pygame.sprite.Sprite):
    
    def __init__(self, x, y, width, height, color=BLACK):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(color)

        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)


# ---------------------------------------------------------

#Lenght of Paddle
class Paddle(BlockSprite):
    def __init__(self, x, y,length):
        
        super().__init__(x, y-75, 10,length, BLUE)  # paddle width & height
    def updatePaddle(self,x,y,length):
        if length <= 50:
            super().__init__(x, y-75, 10,50, BLUE)
        else :
            super().__init__(x, y-75, 10,length, BLUE)
        
    def move(self, step):
        if pygame.sprite.collide_rect(self, top) and (step < 0):  # at top & going up
            step = 0
        elif pygame.sprite.collide_rect(self, bottom) and (step > 0):  
            # at bottom and going down
            step = 0
        self.rect.y += step


# ---------------------------------------------------------

class BallSprite(pygame.sprite.Sprite):

    def __init__(self, fnm):
        super().__init__()
        self.image = pygame.image.load(fnm).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = [scrWidth/2, scrHeight/2]
                       # start position of the ball in center of window
        self.xStep, self.yStep = self.randomSteps()
                       # step size and direction along each axis

    def update(self):
        global scoreLeft, scoreRight
        if pygame.sprite.collide_rect(self, leftPaddle) and (self.xStep < 0):  
            # hit left paddle and going left
            self.xStep = -self.xStep    # change direction

        elif pygame.sprite.collide_rect(self, rightPaddle) and (self.xStep > 0):  
            # hit right paddle and going right
            self.xStep = -self.xStep    # change direction

        if pygame.sprite.spritecollideany(self, horizWalls):
            # change y-step direction at top and bottom sides
            self.yStep = -self.yStep

        if pygame.sprite.spritecollideany(self, vertWalls):
            # ball has reached left or right sides
            if pygame.sprite.collide_rect(self, right):
                scoreLeft += 1
                            
            else:   # left side
                scoreRight += 1  

            # reset the ball
            self.rect.center = (scrWidth/2, scrHeight/2)
            self.xStep, self.yStep = self.randomSteps()

        self.rect.x += self.xStep   # move the ball horizontally
        self.rect.y += self.yStep   # and vertically
        

    def randomSteps(self):
        # create a random +/- STEP pair
        x = STEP
        if random.random() > 0.5:
            x = -x
        y = STEP
        if random.random() > 0.5:
            y = -y
        return [x,y]



# -----------------------------------

def centerImage(screen, im):
    x = (scrWidth - im.get_width())/2
    y = (scrHeight - im.get_height())/2
    screen.blit(im, (x,y))


# ---------- main -------------

pygame.init()

#(1.1) Increase the size of the game area from size of [640,480] to [900,600]
screen = pygame.display.set_mode([900,600])
screen.fill(WHITE)
pygame.display.set_caption("MegaPong")

scrWidth, scrHeight = screen.get_size()

# create wall sprites
top    = BlockSprite(0, 0, scrWidth, WALL_SIZE)
bottom = BlockSprite(0, scrHeight-WALL_SIZE, scrWidth, WALL_SIZE)
left   = BlockSprite(0, 0, WALL_SIZE, scrHeight)
right  = BlockSprite(scrWidth-WALL_SIZE, 0, WALL_SIZE, scrHeight)

horizWalls = pygame.sprite.Group(top, bottom)
vertWalls = pygame.sprite.Group(left, right)

# create two paddles
leftPaddle = Paddle(50, scrHeight/2,200)
rightPaddle = Paddle(scrWidth-50, scrHeight/2,200)

ball01 = BallSprite('smallBall.png')
ball02 = BallSprite('smallBall.png')
ball03 = BallSprite('smallBall.png')
sprites = pygame.sprite.OrderedUpdates(top, bottom, left, right, 
                               leftPaddle, rightPaddle, ball01)

# game vars
leftStep = 0; rightStep = 0
  # move step in pixels for paddles
scoreLeft = 0; scoreRight = 0
winMsg = ""
gameOver = False

# font = pygame.font.Font(None, 30)
font = pygame.font.Font(None, 72)



clock = pygame.time.Clock()
running = True
timetick = 0
tick = 30
time = 0
newscoreLeft = 1
newscoreRight = 1
sumscore = 0
while running:
    
    #(2) the ball gradually move faster as the game playing time increases
    #tick += 0.05
    clock.tick(tick)
    
    
    # handle events
    for event in pygame.event.get():
        if event.type == QUIT: 
            running = False
    
        if event.type == KEYDOWN:
            if event.key == K_q:   # left paddle
                leftStep = -PADDLE_STEP    # up
            elif event.key == K_s:
                leftStep = PADDLE_STEP     # down

            if event.key == K_p:   # right paddle
                rightStep = -PADDLE_STEP   # up
            elif event.key == K_l:
                rightStep = PADDLE_STEP    # down

        elif event.type == KEYUP: 
            if event.key == K_q or event.key == K_s:   # left paddle
                leftStep = 0
            if event.key == K_p or event.key == K_l:   # right paddle
                rightStep = 0

        
    
    # update game
    if not gameOver:
        leftPaddle.move(leftStep)
        rightPaddle.move(rightStep)
        #One Ball
        ball01.update()
        if sumscore < scoreLeft + scoreRight :
            sumscore = scoreLeft + scoreRight
            tick = 30
        else :
            tick += 0.05
            
        timetick += 1
        time = timetick/30

        #(4) the number of balls increases to two, and finally to three by the allotted time.
        #Two Ball
        if time >= 20:
            sprites = pygame.sprite.OrderedUpdates(top, bottom, left, right, 
                               leftPaddle, rightPaddle, ball01,ball02)
            ball02.update()
            
        #Three Ball
        if time >= 30:
            sprites = pygame.sprite.OrderedUpdates(top, bottom, left, right, 
                               leftPaddle, rightPaddle, ball01,ball02,ball03)
            ball03.update()
        if scoreLeft >= WINNING_SCORE:
            winMsg = "Left Wins!"
            gameOver = True
        elif scoreRight >= WINNING_SCORE:
            winMsg = "Right Wins!"
            gameOver = True

        #(3) When score increases, the length of their paddle decreases
        if scoreLeft ==  newscoreLeft:
            newscoreLeft += 1
            leftPaddle.updatePaddle(50, scrHeight/2,200-newscoreLeft*10)
        if scoreRight == newscoreRight:
            newscoreRight += 1
            rightPaddle.updatePaddle(scrWidth-50, scrHeight/2,200-newscoreRight*10)
        
    else :
        time = time
   


    # redraw
    screen.fill(WHITE)                       
    sprites.draw(screen);
    
    screen.blit( font.render(str(scoreLeft) + ":" + 
                             str(scoreRight), True, RED), [20, 20])
    screen.blit( font.render("Time(s) : " + 
                            str('%.1f'%time), True, RED), [500, 20])
    if time >= 30 :
        screen.blit( font.render("Ball = 3", True, RED), [200, 20])
    elif time >= 20 :
        screen.blit( font.render("Ball = 2", True, RED), [200, 20])
    else :
        screen.blit( font.render("Ball = 1", True, RED), [200, 20])
    
    if gameOver:
        centerImage(screen, font.render(winMsg, True, RED))
        
        
    pygame.display.update()

pygame.quit()
