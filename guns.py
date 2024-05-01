from imgs import imagens as imgs
import pygame

class Arma:
    VELOCIDADE = 2
    IMAGEM = pygame.transform.flip(imgs.IMAGEM_ARMA, True, False)

    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def mover(self):
        self.x -= self.VELOCIDADE

    def lock(self, nave):
        self.x = nave.x + 45
        self.y = nave.y + 35
    
    def atirar(self, projeteis): #
        projetil = Projetil(self.x +100, self.y +200)  # Cria um novo projetil na posição da nave
        projeteis.append(projetil)  # Adiciona o projetil à lista de projeteis

    def desenhar(self, tela):
        pos_centro_imagem = self.IMAGEM.get_rect(topleft=(self.x, self.y)).center
        tela.blit(self.IMAGEM, pos_centro_imagem)
    
    def get_mask(self):
        return pygame.mask.from_surface(self.IMAGEM)
    
class Projetil:
    TIRO = imgs.IMAGEM_PROJETIL
    #animações de rotação
    TEMPO_ANIMACAO = 5

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.angulo = 0
        self.velocidade = 0
        self.altura = self.y
        self.tempo = 0
        self.imagem = self.TIRO
    
    def calcular_dano(self):
        return 20  # Ou qualquer outro valor que desejar
        
    def mover(self):
        #calcular deslocamento
        deslocamento = 3
        self.velocidade = 15
        self.x += deslocamento
        
    def desenhar(self, tela):
        #desenhar a imagem
        pos_centro_imagem = self.imagem.get_rect(topleft=(self.x, self.y)).center
        retangulo = self.imagem.get_rect(center=pos_centro_imagem)
        tela.blit(self.imagem, retangulo)

    def get_mask(self):
        return pygame.mask.from_surface(self.imagem)