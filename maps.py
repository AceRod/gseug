from assets.imgs import imagens as imgs

class Chao:
    VELOCIDADE = 5
    LARGURA = imgs.IMAGEM_CHAO[0].get_width()
    ALTURA = imgs.IMAGEM_CHAO[0].get_height()
    IMAGEM = imgs.IMAGEM_CHAO[0]
    TELA_ALTURA = 800

    def __init__(self, y):
        self.y = y
        self.x = 0
        self.x1 = self.LARGURA
        self.x2 = self.LARGURA * 2
        self.x3 = self.LARGURA * 3
        self.x4 = self.LARGURA * 4
        self.x5 = self.LARGURA * 5


    def mover(self):
        self.x1 -= self.VELOCIDADE
        self.x2 -= self.VELOCIDADE
        self.x3 -= self.VELOCIDADE
        self.x4 -= self.VELOCIDADE
        self.x5 -= self.VELOCIDADE

        if self.x1 + self.LARGURA < 0:
            self.x1 = self.x2 + self.LARGURA
        
        if self.x2 + self.LARGURA < 0:
            self.x2 = self.x1 + self.LARGURA

        if self.x3 + self.LARGURA < 0:
            self.x3 = self.x4 + self.LARGURA
        
        if self.x2 + self.LARGURA < 0:
            self.x2 = self.x1 + self.LARGURA

    def desenhar(self, tela):
        for x in range (15):
            tela.blit(self.IMAGEM, ((x * self.LARGURA) - self.VELOCIDADE * 2.5, self.TELA_ALTURA - self.ALTURA))
        #tela.blit(self.IMAGEM, (self.x, self.y))


class Fundo:
    VELOCIDADE = 2
    LARGURA = imgs.IMAGEM_BACKGROUND.get_width()
    IMAGEM = imgs.IMAGEM_BACKGROUND

    def __init__(self):
        self.y = 0
        self.x = 0

    def mover(self):
        self.x -= self.VELOCIDADE

    def desenhar(self, tela):
        tela.blit(self.IMAGEM, (self.x, self.y))