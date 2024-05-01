from imgs import imagens as imgs

class Chao:
    VELOCIDADE = 5
    LARGURA = imgs.IMAGEM_CHAO[0].get_width()
    IMAGEM = imgs.IMAGEM_CHAO[0]

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
        tela.blit(self.IMAGEM, (self.x, self.y))
        tela.blit(self.IMAGEM, (self.x1, self.y))
        tela.blit(self.IMAGEM, (self.x2, self.y))
        tela.blit(self.IMAGEM, (self.x3, self.y))
        tela.blit(self.IMAGEM, (self.x4, self.y))
        tela.blit(self.IMAGEM, (self.x5, self.y))

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