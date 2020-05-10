import pygame
from pygame.locals import *

BLACK = (   0,   0,   0)
WHITE = ( 255, 255, 255)
RED = (255,0,0)

def draw_stick_figure(screen, x, y):
    # Head
    pygame.draw.ellipse(screen, BLACK, [1 + x, y, 10, 10], 0)

    # Legs
    pygame.draw.line(screen, BLACK, [5 + x, 17 + y], [10 + x, 27 + y], 2)
    pygame.draw.line(screen, BLACK, [5 + x, 17 + y], [x, 27 + y], 2)

    # Body
    pygame.draw.line(screen, RED, [5 + x, 17 + y], [5 + x, 7 + y], 2)

    # Arms
    pygame.draw.line(screen, RED, [5 + x, 7 + y], [9 + x, 17 + y], 2)
    pygame.draw.line(screen, RED, [5 + x, 7 + y], [1 + x, 17 + y], 2)

def limitPos(screen, x, y):
    width, height = screen.get_size()
    if (x < 0):
        x = 0
    elif (x > width-1 - 10):   # add in stick figure max width
        x = width-1 - 10

    if (y < 0):
        y = 0
    elif (y > height-1 - 27):  #add in stick figure max height
        y = height-1 - 27
    return (x, y)


pygame.init()
screen = pygame.display.set_mode([700, 500])
pygame.display.set_caption("Move Mouse")

clock = pygame.time.Clock()

# Hide the mouse cursor
pygame.mouse.set_visible(0)

running = True
while running:
    clock.tick(30)

    for event in pygame.event.get(): 
        if event.type == QUIT: 
            running = False


        if event.type == MOUSEBUTTONDOWN and \
           pygame.mouse.get_pressed()[1]:   # middle button pressed
            running = False


    pos = pygame.mouse.get_pos()    # pos is [x, y] of mouse
    x, y = limitPos(screen, pos[0], pos[1])

    # redraw
    screen.fill(WHITE)
    draw_stick_figure(screen, x, y)  
    pygame.display.update()
     
pygame.quit()
