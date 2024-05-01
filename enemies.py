from imgs import imagens as imgs
import random
import pygame

class Inimigos:
    IMGS = imgs.IMAGENS_INIMIGOS
    DISTANCIA = 200
    VELOCIDADE = 5

    def __init__(self, x):
        self.x = x
        self.altura = 0
        self.imagem = self.IMGS[0]
        self.passou = False
        #self.reposicionar()
        self.definir_altura()
        self.hp = 100

    def definir_altura(self):
        self.altura = random.randrange(150, 650)

    def get_y(self):
        self.y = self.altura
       

    def mover(self):
        self.x -= self.VELOCIDADE

    def desenhar(self, tela):
        # pos_centro_imagem = self.imagem.get_rect(topleft=(self.x, self.altura)).center
        # tela.blit(self.imagem, pos_centro_imagem)
        pos_centro_imagem = self.imagem.get_rect(topleft=(self.x, self.altura)).center
        retangulo = self.imagem.get_rect(center=pos_centro_imagem)
        tela.blit(self.imagem, retangulo)

    def colidir(self, projetil):
        projetil_mask = projetil.get_mask()
        mask = pygame.mask.from_surface(self.imagem)

        dano = (self.x - projetil.x, self.altura - round(projetil.y))
        colisao = projetil_mask.overlap(mask, dano)


        if colisao:
            dano_causado = projetil.calcular_dano()
            self.hp -= dano_causado
            return True
        else:
            return False