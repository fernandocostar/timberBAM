from PPlay.window import Window
from PPlay.gameimage import GameImage
from arvore import Arvore
from bodybuilder import BodyBuilder
from pontuador import Pontuador
from highscoremanager import ScoreManager

janela = Window(512, 512)
janela.set_title('TimberBAM')

background = GameImage('sprite/cenario/cenarionew.png')
menu_bg = GameImage('sprite/cenario/start.png')
botao_inicial = GameImage('sprite/cenario/botao.png')
tela_final = GameImage('sprite/cenario/GAMEOVER.png')
score_manager = ScoreManager()

teclado = janela.get_keyboard()

arvore = Arvore(janela)
bambam = BodyBuilder(janela, 'esquerda')
pontuador = Pontuador(janela)

teclado_pressionado = False
record_checked = False

game_state = 2  # 0 - JOGANDO  1 - GAME-OVER  2- IN-MENU

while True:
    if game_state == 0:
        if teclado.key_pressed('left') or teclado.key_pressed('right'):
            if not teclado_pressionado:
                lado = 1 if teclado.key_pressed('left') else 0
                lado_bambam = 'esquerda' if teclado.key_pressed('left') else 'direita'
                lado_atingido_1, lado_atingido_2 = arvore.hit(lado)
                bambam.hit(lado_bambam)
                pontuador.pontuar()
                if lado == lado_atingido_1 or lado == lado_atingido_2:
                    game_state = 1
            teclado_pressionado = True
        else:
            teclado_pressionado = False
        background.draw()
        arvore.update()
        arvore.draw()
        bambam.update()
        bambam.draw()
        pontuador.update()
        if not pontuador.bambam_alive():
            game_state = 1
        pontuador.draw()

    elif game_state == 1:
        if not record_checked:
            if pontuador.get_pontuacao() > score_manager.get_recorde():
                score_manager.set_new_record(pontuador.get_pontuacao())
            record_checked = True

        background.draw()
        arvore.draw()
        tela_final.draw()
        janela.draw_text(str(score_manager.get_recorde()), 260, 205, color=(20, 200, 50), font_file='font.TTF',
                         size=30)
        janela.draw_text(str(pontuador.get_pontuacao()), 260, 240, color=(20, 200, 50), font_file='font.TTF',
                         size=30)
        if teclado.key_pressed('enter'):
            game_state = 0
            arvore = Arvore(janela)
            bambam = BodyBuilder(janela, 'esquerda')
            pontuador = Pontuador(janela)
            record_checked = False

    elif game_state == 2:
        menu_bg.draw()
        botao_inicial.draw()
        janela.draw_text(str(score_manager.get_recorde()), 512 - 56, 274, color=(20, 200, 50), font_file='font.TTF', size=30)
        if teclado.key_pressed('enter'):
            game_state = 0
    janela.update()

