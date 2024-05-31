from assets.imgs import imagens as imgs
import pygame
import guns

class Nave:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.velocidade = 0
        self.altura = self.y
        self.tempo = 0
        self.imagem = imgs.IMAGEMS_NAVES[0]

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
    
#utilizando o conceito de herença e polimorfirsmo
class Enemy(Nave):
    def __init__(self, x, y) -> None:
        super().__init__(x, y)
        self.imagem = imgs.IMAGENS_INIMIGOS[0]
        self.velocidade = 5
        self.hp = 100

    def mover(self):
        self.x -= self.velocidade
    
    # def desenhar(self, tela):
    #      # pos_centro_imagem = self.imagem.get_rect(topleft=(self.x, self.altura)).center
    #      # tela.blit(self.imagem, pos_centro_imagem)
    #      pos_centro_imagem = self.imagem.get_rect(topleft=(self.x, self.y)).center
    #      retangulo = self.imagem.get_rect(center=pos_centro_imagem)
    #      tela.blit(self.imagem, retangulo)