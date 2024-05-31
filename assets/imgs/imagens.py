import pygame
import os

IMAGEMS_NAVES = [
    pygame.transform.scale2x(pygame.image.load(os.path.join('assets\imgs', '2ndship.png'))),
    pygame.image.load(os.path.join('assets\imgs', 'nave.png')),
]
IMAGEM_ARMA = pygame.image.load(os.path.join( 'assets\imgs','arma.png'))
IMAGEM_BACKGROUND = pygame.image.load(os.path.join('assets\imgs','cyberpunk.png'))
IMAGEM_PROJETIL = pygame.image.load(os.path.join('assets\imgs', 'projetil.png'))
IMAGEM_CHAO =  [
    pygame.image.load(os.path.join('assets\imgs', 'base.png')), 
    #pygame.image.load(os.path.join('assets\imgs', 'floor.png'))
]
IMAGENS_INIMIGOS = [
    pygame.image.load(os.path.join('assets\imgs', 'boss.png')),
    #pygame.transform.scale2x(pygame.image.load(os.path.join('FlappyBird\spaceship', 'monstro.png')))
]
