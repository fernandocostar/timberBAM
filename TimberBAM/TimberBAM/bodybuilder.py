from PPlay.gameimage import GameImage


class BodyBuilder:
    def __init__(self, janela, lado):
        self.lado = lado
        self.janela = janela
        self.sprites = (GameImage('sprite/bambam/be1.png', 0, 512 - 150),
                        GameImage('sprite/bambam/be3.png', 0, 512 - 150),
                        GameImage('sprite/bambam/bd1.png', 0, 512 - 150),
                        GameImage('sprite/bambam/bd3.png', 0, 512 - 150))
        self.batendo = False
        self.sprite_atual = 0
        self.tempo_soco = 0

    def get_lado(self):
        return 1 if self.lado == 'esquerda' else 0

    def hit(self, lado):
        if self.lado != lado:
            if self.sprite_atual == 0:
                self.sprite_atual = 2
            else:
                self.sprite_atual = 0
            self.batendo = True
            self.tempo_soco = self.janela.total_time
        else:
            self.batendo = True
            self.tempo_soco = self.janela.total_time
        self.lado = lado

    def draw(self):
        self.sprites[self.sprite_atual].draw()

    def update(self):
        if self.batendo:
            if self.janela.total_time - self.tempo_soco > 5:
                if self.lado == 'esquerda':
                    self.sprite_atual = 1
                else:
                    self.sprite_atual = 3
            if self.janela.total_time - self.tempo_soco > 50:
                self.batendo = False
                if self.lado == 'esquerda':
                    self.sprite_atual = 0
                else:
                    self.sprite_atual = 2
