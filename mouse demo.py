import pygame
from pygame.locals import *

BLACK = (   0,   0,   0)
WHITE = ( 255, 255, 255)

pygame.init()
screen = pygame.display.set_mode([340,240])
pygame.display.set_caption("Mouse Demo")

clock = pygame.time.Clock()

# Hide the mouse cursor
pygame.mouse.set_visible(0)

running = True
while running:
    clock.tick(30)
    for event in pygame.event.get(): 
        if event.type == QUIT: 
            running = False
        if event.type == MOUSEBUTTONDOWN: #รอรับคำสั่งจาก mouse (1,0,0) => mouse ซ้าย , (0,0,1) => mouse ขวา
            print('    Pressed:', 
                    pygame.mouse.get_pressed())
        elif event.type == MOUSEBUTTONUP:
            print('        Released:', 
                    pygame.mouse.get_pressed())
        if event.type == MOUSEMOTION:
            print('Move:', pygame.mouse.get_rel())

    # redraw
    screen.fill(WHITE)

    # draw a circle around the mouse pointer จะมีการ Update ข้อมูลจาก mouse
    pos = ( pygame.mouse.get_pos()[0], 
            pygame.mouse.get_pos()[1])
    pygame.draw.circle(screen, BLACK, pos, 5, 0)

    pygame.display.update()
     
pygame.quit() 
