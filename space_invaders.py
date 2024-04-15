import pygame
import os
import random

TELA_LARGURA = 1500
TELA_ALTURA = 800


IMAGEMS_NAVES = [
    pygame.transform.scale2x(pygame.image.load(os.path.join('Shootem_up\spaceship', '2ndship.png'))),
    pygame.image.load(os.path.join('Shootem_up\spaceship', 'nave.png')),
]
IMAGEM_ARMA = pygame.image.load(os.path.join('Shootem_up\spaceship', 'arma.png'))
IMAGEM_BACKGROUND = pygame.image.load(os.path.join('Shootem_up\spaceship', 'cyberpunk.png'))
IMAGEM_PROJETIL = pygame.image.load(os.path.join('Shootem_up\spaceship', 'projetil.png'))
IMAGEM_CHAO =  pygame.transform.scale2x(pygame.image.load(os.path.join('Shootem_up\imgs', 'base.png')))
IMAGENS_INIMIGOS = [
    pygame.image.load(os.path.join('Shootem_up\spaceship', 'boss.png')),
    #pygame.transform.scale2x(pygame.image.load(os.path.join('FlappyBird\spaceship', 'monstro.png')))
]

pygame.font.init()
FONTE_PONTOS = pygame.font.SysFont('arial', 50)
FONTE_ERROS = pygame.font.SysFont('arial', 50)


class Nave:
    NAVE = IMAGEMS_NAVES[0]
    TIRO = IMAGEM_PROJETIL
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
        projetil = Projetil(self.x +140, self.y +70)  # Cria um novo projetil na posição da nave
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
    
    # def encontrar(self, arma):
    #     arma_mask = arma.get_mask()
    #     nave_mask = pygame.mask.from_surface(self.imagem)

    #     encontro = (self.x - arma.x, self.altura - round(arma.y))

    #     captura = nave_mask.overlap(arma_mask, encontro)


    #     if captura:
    #         return True
    #     else:
    #         return False
class Arma:
    VELOCIDADE = 2
    IMAGEM = pygame.transform.flip(IMAGEM_ARMA, True, False)

    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def mover(self):
        self.x -= self.VELOCIDADE

    def lock(self, nave):
        self.x = nave.x + 45
        self.y = nave.y + 35
        self.IMAGEM = pygame.transform.flip(self.IMAGEM, True, False)
    
    def atirar(self, projeteis): #
        projetil = Projetil(self.x +100, self.y +200)  # Cria um novo projetil na posição da nave
        projeteis.append(projetil)  # Adiciona o projetil à lista de projeteis

    def desenhar(self, tela):
        pos_centro_imagem = self.IMAGEM.get_rect(topleft=(self.x, self.y)).center
        tela.blit(self.IMAGEM, pos_centro_imagem)
    
    def get_mask(self):
        return pygame.mask.from_surface(self.IMAGEM)
    
class Projetil:
    TIRO = IMAGEM_PROJETIL
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


class Inimigos:
    IMGS = IMAGENS_INIMIGOS
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
        pos_centro_imagem = self.imagem.get_rect(topleft=(self.x, self.altura)).center
        tela.blit(self.imagem, pos_centro_imagem)

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


class Chao:
    VELOCIDADE = 5
    LARGURA = IMAGEM_CHAO.get_width()
    IMAGEM = IMAGEM_CHAO

    def __init__(self, y):
        self.y = y
        self.x0 = 0
        self.x1 = self.LARGURA
        self.x2 = self.LARGURA
        self.x3 = self.LARGURA
        self.x4 = self.LARGURA

    def mover(self):
        self.x1 -= self.VELOCIDADE
        self.x2 -= self.VELOCIDADE
        self.x3 -= self.VELOCIDADE
        self.x4 -= self.VELOCIDADE

        if self.x1 + self.LARGURA < 0:
            self.x1 = self.x2 + self.LARGURA
        
        if self.x2 + self.LARGURA < 0:
            self.x2 = self.x1 + self.LARGURA

    def desenhar(self, tela):
        tela.blit(self.IMAGEM, (self.x1, self.y))
        tela.blit(self.IMAGEM, (self.x2, self.y))

class Fundo:
    VELOCIDADE = 2
    LARGURA = IMAGEM_BACKGROUND.get_width()
    IMAGEM = IMAGEM_BACKGROUND

    def __init__(self):
        self.y = 0
        self.x = 0

    def mover(self):
        self.x -= self.VELOCIDADE

    def desenhar(self, tela):
        tela.blit(self.IMAGEM, (self.x, self.y))

def desenhar_tela(tela, fundo, naves, armas,  projeteis, inimigos, chao, pontos, danos, arma_travada):
    #tela.blit(IMAGEM_BACKGROUND, (0 , 0))
    fundo.desenhar(tela)

    for arma in armas:
        arma.desenhar(tela)
        arma.mover()
    for nave in naves:
        nave.desenhar(tela)
    for inimigo in inimigos:
        inimigo.desenhar(tela)
        inimigo.mover()
    for projetil in projeteis:
        projetil.desenhar(tela)
        projetil.mover()

    texto = FONTE_PONTOS.render(f'Pontuação: {pontos}', 1, (255, 255, 255))
    cont_dano = FONTE_ERROS.render(f'Dano: {danos}', 1, (255, 1, 1))  # Usando danos[0]
    arma_travada = FONTE_PONTOS.render(f'Arma Travada: {arma_travada}',  1, (255, 1, 255))
    tela.blit(texto, (TELA_LARGURA - 10 - texto.get_width(), 10))
    tela.blit(cont_dano, (10, 10))
    tela.blit(arma_travada, (200, 10))
    chao.desenhar(tela)
    pygame.display.update()

def main():
    naves = [Nave(230,350)]
    armas = [Arma(1400, 500) ] #Arma(1400, 500)
    projeteis = []
    chao = Chao(730)
    fundo = Fundo()
    inimigos = [Inimigos(1400)]
    tela = pygame.display.set_mode((TELA_LARGURA, TELA_ALTURA))
    pontos = 0
    danos = 0
    relogio = pygame.time.Clock()
    

    rodando = True
    while rodando:
        relogio.tick(30)
        fundo.mover()
        arma_travada = False
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
                pygame.quit()
                quit()

            for nave in naves:
                for arma in armas:
                    if evento.type == pygame.KEYDOWN:
                        if evento.key == pygame.K_SPACE:
                            if arma_travada == True:
                                arma.atirar(projeteis)
                            elif arma_travada == False:
                                nave.atirar(projeteis)

        teclas = pygame.key.get_pressed()

        for nave in naves:
            if teclas[pygame.K_UP] or teclas[pygame.K_w]:
                nave.y -= 10
            elif teclas[pygame.K_DOWN] or teclas[pygame.K_s]:
                nave.y += 10
            elif teclas[pygame.K_LEFT] or teclas[pygame.K_a]:
                nave.x -= 10
            elif teclas[pygame.K_RIGHT] or teclas[pygame.K_d]:
                nave.x += 10

        for nave in naves:
            nave.mover()
        chao.mover()

        adicionar_inimigo = False
        remover_inimigos = []
        for inimigo in inimigos:
            for i, projetil in enumerate(projeteis):
                if inimigo.colidir(projetil):
                    projeteis.pop(i)
                    if inimigo.hp <= 0:
                        remover_inimigos.append(inimigo)
                        pontos += 50
                        adicionar_inimigo = True

        if adicionar_inimigo:
            inimigos.append(Inimigos(1400))

        for inimigo in remover_inimigos:
            inimigos.remove(inimigo)
            armas.append(Arma(inimigo.x, inimigo.altura))
        
        for  arma in armas:
            for nave in naves:
                if nave.get_mask().overlap(arma.get_mask(), (arma.x - nave.x, arma.y -  nave.y)):
                    arma.lock(nave)
                    arma_travada = True

        desenhar_tela(tela, fundo, naves, armas, projeteis, inimigos, chao, pontos, danos, arma_travada)

if __name__ == '__main__':
    main() 