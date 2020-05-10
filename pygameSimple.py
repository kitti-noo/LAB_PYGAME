
# pygameSimple.py

import pygame
from pygame.locals import *
#Define กำหนด
GREEN = (0,255,0)
BLACK = (0,0,0)
BLUE = (0,0,255)
MUSTARD = (204,204,0)
RED = (255,0,0)
pi = 22/7
def drawStuff(screen):

    # draw a green line
    pygame.draw.line(screen, GREEN, (0, 0), (100, 100), 5)#เส้น
    pygame.draw.rect(screen, BLACK, (20, 20, 250, 100), 2) #สี่เหลี่ยม
    pygame.draw.circle(screen, BLUE, (340, 60), 40, 3 ) #วงกลม
    pygame.draw.ellipse(screen, MUSTARD, (400,20,150,100), 0) #วงรี
    #เส้นโค้ง
    pygame.draw.arc(screen, BLACK,(20, 220, 250, 200), 0, pi/2,10)
    pygame.draw.arc(screen, GREEN,(20, 220, 250, 200), pi/2, pi,10)
    pygame.draw.arc(screen, BLUE, (20, 220, 250, 200), pi, 3*pi/2, 10)
    pygame.draw.arc(screen, RED, (20, 220, 250, 200), 3*pi/2, 2*pi,10)
    #Polygon
    points = ( (237, 372), (332, 319),
               (483, 335), (422, 389),
               (447, 432), (359, 379),
               (320, 439), (232, 392) )
    pygame.draw.polygon(screen, GREEN, points, 0)

    #Using the Default font
    # 1. load default font; 48pt size  กำหนดขนาดของ font
    font = pygame.font.Font(None, 48)
 
    # 2. render anti-aliased (smooth) black text as an image แปลง font เป็นรูปภาพ
    textImage = font.render("Hello World", True, RED)

    # 3. draw text image with its top-left corner at (270,250) แสดงรูปภาพมาทางหน้าจอ
    screen.blit(textImage, (270, 250))






pygame.init()

screenSize = (640, 480) #ขนาดหน้าจอ
screen = pygame.display.set_mode(screenSize) #แสดงหน้าจอ
screen.fill((0,200,255))    # white background

pygame.display.set_caption("Hello, Pygame!")  # set title bar
drawStuff(screen)


clock = pygame.time.Clock() #ตัวจับเวลา

running = True
while running:  # game loop
    time_passed = clock.tick(30)   # set loop speed or Frame rate

    # handle events #read รอรับ event จากผู้ใช้
    for event in pygame.event.get():
        if event.type == QUIT:     # user clicks close box
            running = False
        if (event.type == KEYUP and event.key == K_ESCAPE): # KEYUP : กดแล้วปล่อย , K_ESCAPE : ปุ่ม ESC
            running = False
                                    # user clicks <ESC> key


    # update game state  (nothing yet)

    # redraw game # render ภาพ
    pygame.display.update()

pygame.quit()
