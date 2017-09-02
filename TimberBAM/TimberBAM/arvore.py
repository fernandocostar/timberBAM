from PPlay.gameimage import GameImage
from random import randint


class GalhoVoador:
    def __init__(self, janela, galho, lado):
        self.janela = janela
        self.galho = galho
        self.lado = lado
        self.angulo = 200 if lado == 1 else 160
        self.galho.set_position(self.galho.get_x(), self.galho.get_y() - 64)

    def update(self):
        if self.lado == 1:
            self.galho.set_position(self.galho.get_x() + (2000 * self.janela.delta_time()), self.galho.get_y())
            self.angulo -= 270 * self.janela.delta_time()
        else:
            self.galho.set_position(self.galho.get_x() - (2000 * self.janela.delta_time()), self.galho.get_y())
            self.angulo += 270 * self.janela.delta_time()

    def draw(self):
        self.galho.draw_rotated(self.angulo)

    def fora_da_tela(self):
        return self.galho.get_x() > 300 or self.galho.get_x() < -300


class Galho:
    def __init__(self, lado, x, y):
        image_paths = ('sprite/galhos/galhodireitanew.png',
                       'sprite/galhos/galhoesquerdanew.png',
                       'sprite/galhos/semgalho.png')
        self.texture = GameImage(image_paths[lado])
        self.lado = lado
        self.texture.set_position(x, y)

    def set_position(self, x, y):
        self.texture.set_position(x, y)

    def get_lado(self):
        return self.lado

    def draw(self):
        self.texture.draw()

    def draw_rotated(self, angle):
        self.texture.draw_rotated(angle)

    def get_x(self):
        return self.texture.x

    def get_y(self):
        return self.texture.y


class Arvore:
    def __init__(self, janela):
        self.time_hit = 0
        self.janela = janela
        self.descendo = False

        self.lado_ultimo_galho = 'meio'
        self.galhos_voadores = []
        self.galhos = []
        self.galhos.append(Galho(2, 0, 512 - 128))
        self.last_galho = 2
        for i in range(1, 7):
            lado = randint(0, 2)
            if self.galhos[-1].get_lado() != 2 and self.galhos[-1].get_lado() != lado:
                lado = 2
            self.galhos.append(Galho(lado, 0, 512 - 128 - i * 64))
            self.last_galho = lado

    def draw(self):
        for galho in self.galhos:
            galho.draw()
        for galho in self.galhos_voadores:
            galho.draw()

    def hit(self, lado):
        if not self.descendo:
            self.time_hit = self.janela.total_time
            self.descendo = True
            lado_galho = self.galhos[0].get_lado()
            lado_galho_2 = self.galhos[1].get_lado()
            self.galhos_voadores.append(GalhoVoador(self.janela, self.galhos.pop(0), lado))
            lado = randint(0, 2)
            if self.galhos[-1].get_lado() != 2 and self.galhos[-1].get_lado() != lado:
                lado = 2
            self.galhos.append(Galho(lado, 0, -64))
            self.last_galho = lado
            return lado_galho, lado_galho_2

    def update(self):
        if self.descendo and self.janela.total_time - self.time_hit > 30:
            for galho in self.galhos:
                galho.set_position(0, galho.get_y() + 64)
            self.descendo = False
        tbd = []
        for i, galho in enumerate(self.galhos_voadores):
            if galho.fora_da_tela():
                tbd.append(i)
            galho.update()
        for j in reversed(tbd):
            del self.galhos_voadores[j]
