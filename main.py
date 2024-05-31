import pygame
import maps
import spaceships as sp
import guns
import random

# Configuração da tela
TELA_LARGURA = 1500
TELA_ALTURA = 800

pygame.font.init()
FONTE_PONTOS = pygame.font.SysFont('arial', 50)
FONTE_ERROS = pygame.font.SysFont('arial', 50)

class HealthBar():
    def __init__(self, x, y, w, h, max_hp):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.hp = max_hp
        self.max_hp = max_hp

    def desenhar(self, tela):
        #calcular a porcentagem do hp
        ratio = self.hp / self.max_hp
        pygame.draw.rect(tela, "red", (self.x,self.y,self.w,self.h))
        pygame.draw.rect(tela, "Green", (self.x,self.y,self.w * ratio,self.h))

def desenhar_tela(tela, fundo, naves , inimigos, armas, projeteis,  chao, pontos, healthBar):
    fundo.desenhar(tela)
    healthBar.desenhar(tela)

    for arma in armas:
        arma.desenhar(tela)
        arma.mover()
         
    for nave in naves:
        nave.desenhar(tela)
        nave.mover()

    for inimigo in inimigos:
        inimigo.desenhar(tela)
        inimigo.mover()

    for projetil in projeteis:
        projetil.desenhar(tela)
        projetil.mover()

    texto = FONTE_PONTOS.render(f'Pontuação: {pontos}', 1, (255, 255, 255))
    tela.blit(texto, (TELA_LARGURA - 10 - texto.get_width(), 10))
    #cont_dano = FONTE_ERROS.render(f'Dano: {danos}', 1, (255, 1, 1))  # Usando danos[0]
    #arma_travada = FONTE_PONTOS.render(f'Arma Travada: {arma_travada}',  1, (255, 1, 255))
    #tela.blit(cont_dano, (10, 10))
    #tela.blit(arma_travada, (200, 10))
    chao.desenhar(tela)
    pygame.display.update()
    pygame.display.set_caption("GSEUG")



        


def main():
    tela = pygame.display.set_mode((TELA_LARGURA, TELA_ALTURA))
    fundo = maps.Fundo()
    naves = [sp.Nave(230,350)]
    enemie_y = random.randrange(150, 650)
    inimigos = [sp.Enemy(1400, enemie_y)]
    armas = [] #guns.Arma(2900, 500)
    projeteis = []
    chao = maps.Chao(730)
    pontos = 0
    relogio = pygame.time.Clock()
    healthBar = HealthBar(20, 20, 300, 40, 100)
    

    rodando = True
    while rodando:
        relogio.tick(30)
        fundo.mover()
        chao.mover()
        arma_travada = False
        healthBar.hp = 50


        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
                pygame.quit()
                quit()
            if arma_travada:
                for nave in naves:
                    for arma in armas:
                        if evento.type == pygame.KEYDOWN:
                            if evento.key == pygame.K_SPACE:
                                arma.atirar(projeteis)
            if not arma_travada:
                for nave in naves:
                    if evento.type == pygame.KEYDOWN:
                        if evento.key == pygame.K_SPACE:                    
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
            inimigos.append(sp.Enemy(1400,enemie_y))

        for inimigo in remover_inimigos:
            armas.append(guns.Arma(inimigo.x -45, inimigo.altura -35))
            inimigos.remove(inimigo)

        for  arma in armas:
            for nave in naves:
                if nave.get_mask().overlap(arma.get_mask(), (arma.x - nave.x, arma.y -  nave.y)):
                    arma.lock(nave)
                    arma_travada = True

        desenhar_tela(tela, fundo, naves , inimigos, armas, projeteis,  chao, pontos, healthBar)


if __name__ == '__main__':
    main()