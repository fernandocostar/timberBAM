import pygame


class Pontuador:
    def __init__(self, janela):
        self.janela = janela
        self.hp = 100
        self.pontos = 0
        self.multiplicador = 1
        self.taxa_de_perda_de_vida = 3.3

    def pontuar(self):
        self.pontos += 1
        self.hp += 1
        self.taxa_de_perda_de_vida += 0.4 ** self.taxa_de_perda_de_vida
        if self.hp > 100:
            self.hp = 100

    def update(self):
        self.hp -= self.taxa_de_perda_de_vida * self.janela.delta_time()

    def bambam_alive(self):
        return self.hp > 0

    def get_pontuacao(self):
        return self.pontos

    def draw(self):
        pygame.draw.rect(self.janela.get_screen(), (105, 105, 105), (512 / 2 - 66, 8, 132, 34), 0)  # Borda cinza de 2px
        pygame.draw.rect(self.janela.get_screen(), (255, 0, 0), (512 / 2 - 64, 10, 128, 30), 0)  # Barra vermelha
        pygame.draw.rect(self.janela.get_screen(), (0, 255, 0), (512 / 2 - 64, 10,  self.hp / 100 * 128, 30), 0) # Barra verde
        self.janela.draw_text('Pontos: {}'.format(self.pontos), 512 / 2 - 64, 12, color=(0, 0, 255), font_file='font.TTF', size=24)
