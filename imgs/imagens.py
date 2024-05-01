import pygame
import os

IMAGEMS_NAVES = [
    pygame.transform.scale2x(pygame.image.load(os.path.join('Shootem_up\spaceship', '2ndship.png'))),
    pygame.image.load(os.path.join('Shootem_up\spaceship', 'nave.png')),
]
IMAGEM_ARMA = pygame.image.load(os.path.join('Shootem_up\spaceship', 'arma.png'))
IMAGEM_BACKGROUND = pygame.image.load(os.path.join('Shootem_up\spaceship', 'cyberpunk.png'))
IMAGEM_PROJETIL = pygame.image.load(os.path.join('Shootem_up\spaceship', 'projetil.png'))
IMAGEM_CHAO =  [
    pygame.transform.scale2x(pygame.image.load(os.path.join('Shootem_up\imgs', 'base.png'))), 
    #pygame.transform.scale2x(
        pygame.image.load(os.path.join('Shootem_up\imgs', 'floor.png'))
        #)
]
IMAGENS_INIMIGOS = [
    pygame.image.load(os.path.join('Shootem_up\spaceship', 'boss.png')),
    #pygame.transform.scale2x(pygame.image.load(os.path.join('FlappyBird\spaceship', 'monstro.png')))
]