from imgs import imagens as imgs
import pygame
import guns

class Nave:
    NAVE = imgs.IMAGEMS_NAVES[0]  
    TIRO = imgs.IMAGEM_PROJETIL
    #animações de rotação
    ROTACAO_MAXIMA = 25
    VALOCIDADE_ROTACAO = 20
    TEMPO_ANIMACAO = 5

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.angulo = 0
        self.velocidade = 0
        self.altura = self.y
        self.tempo = 0
        self.contagem_imagem = 0
        self.imagem = self.NAVE

    def atirar(self, projeteis): #
        projetil = guns.Projetil(self.x +140, self.y +70)  # Cria um novo projetil na posição da nave
        projeteis.append(projetil)  # Adiciona o projetil à lista de projeteis

    def mover(self):
        #calcular deslocamento
        self.tempo += 1
        deslocamento = 0
        self.y += deslocamento

    def desenhar(self, tela):
        #desenhar a imagem
        pos_centro_imagem = self.imagem.get_rect(topleft=(self.x, self.y)).center
        retangulo = self.imagem.get_rect(center=pos_centro_imagem)
        tela.blit(self.imagem, retangulo)

    def get_mask(self):
        return pygame.mask.from_surface(self.imagem)