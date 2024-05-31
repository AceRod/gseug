import pygame
import os

pygame.init()

#define screen size
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

#cREATE GAME WINDOW
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Space Invaders")

#define colours
BG = (0, 0, 0)
GREEN = (0,255,0)
RED = (255,0,0)
BLUE = (0,0, 255)
WHITE = (255,255,255)

#hide mouse cursor
pygame.mouse.set_visible(False)

#create nave
nave = pygame.transform.scale2x(pygame.image.load(os.path.join('Shootem_up\spaceship','2ndship.png')))
nave_rect = nave.get_rect()
nave_rect.topleft = (x, y)
nave_mask = pygame.mask.from_surface(nave)
mask_image = nave_mask.to_surface()

#Create bullet and mask
bullet = pygame.Surface((10,10))
bullet.fill(RED)
bullet_mask = pygame.mask.from_surface(bullet)

#game loop
running = True
while running:
    #get mouse coordinates
    pos = pygame.mouse.get_pos()

    #update background
    screen.fill(BG)

    #Check mask overlap
    if nave_mask.overlap(bullet_mask, (pos[0] - nave_mask.x, pos[1] - nave_mask.y)):
        col = RED
    else:
        col = GREEN
                         

    #Draw nave
    screen.blit(mask_image,(0, 0))

    #draw rectangle
    screen.blit(bullet, pos)

    #event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    #update display
    pygame.display.flip()

pygame.quit()