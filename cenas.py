from PPlay.mouse import *
from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sound import *

import fase1
import fase2
import fase3
import fase4


def cena_inicial():
    janela = Window(800, 600)
    janela.set_title("Not a Hero!")

    mouse = Mouse()

    fundo = GameImage("imagens/cenas/fundo_inicio.jpg")
    texto = GameImage("imagens/cenas/texto_cena_inicial.png")
    botao_continuar = GameImage("imagens/menu_inicial/botao_continuar.png")

    botao_continuar.x = janela.width / 2 - 80
    botao_continuar.y = janela.height - 50

    while True:
        if mouse.is_button_pressed(1) and mouse.is_over_object(botao_continuar):
            fase1.iniciar_fase1()

        fundo.draw()
        texto.draw()
        botao_continuar.draw()

        janela.update()


def cena_1_boa():
    janela = Window(800, 600)
    janela.set_title("Not a Hero!")

    mouse = Mouse()

    fundo = GameImage("imagens/cenas/fundo_fase1.jpg")
    texto = GameImage("imagens/cenas/texto_cena1_boa.png")
    botao_continuar = GameImage("imagens/menu_inicial/botao_continuar.png")

    botao_continuar.x = janela.width / 2 - 80
    botao_continuar.y = janela.height - 50

    while True:
        if mouse.is_button_pressed(1) and mouse.is_over_object(botao_continuar):
            fase2.iniciar_fase2()

        fundo.draw()
        texto.draw()
        botao_continuar.draw()

        janela.update()


def cena_1_ruim():
    janela = Window(800, 600)
    janela.set_title("Not a Hero!")

    mouse = Mouse()

    fundo = GameImage("imagens/cenas/fundo_fase1.jpg")
    texto = texto = GameImage("imagens/cenas/texto_cena1_ruim.png")
    botao_continuar = GameImage("imagens/menu_inicial/botao_continuar.png")

    botao_continuar.x = janela.width / 2 - 80
    botao_continuar.y = janela.height - 50

    while True:
        if mouse.is_button_pressed(1) and mouse.is_over_object(botao_continuar):
            fase2.iniciar_fase2()

        fundo.draw()
        texto.draw()
        botao_continuar.draw()

        janela.update()


def cena_2_boa():
    janela = Window(800, 600)
    janela.set_title("Not a Hero!")

    mouse = Mouse()

    fundo = GameImage("imagens/cenas/fundo_fase2.jpg")
    texto = GameImage("imagens/cenas/texto_cena2_boa.png")
    botao_continuar = GameImage("imagens/menu_inicial/botao_continuar.png")

    botao_continuar.x = janela.width / 2 - 80
    botao_continuar.y = janela.height - 50

    while True:
        if mouse.is_button_pressed(1) and mouse.is_over_object(botao_continuar):
            fase3.iniciar_fase3()

        fundo.draw()
        texto.draw()
        botao_continuar.draw()

        janela.update()


def cena_2_ruim():
    janela = Window(800, 600)
    janela.set_title("Not a Hero!")

    mouse = Mouse()

    fundo = GameImage("imagens/cenas/fundo_fase2.jpg")
    texto = GameImage("imagens/cenas/texto_cena2_ruim.png")
    botao_continuar = GameImage("imagens/menu_inicial/botao_continuar.png")

    botao_continuar.x = janela.width / 2 - 80
    botao_continuar.y = janela.height - 50

    while True:
        if mouse.is_button_pressed(1) and mouse.is_over_object(botao_continuar):
            fase3.iniciar_fase3()

        fundo.draw()
        texto.draw()
        botao_continuar.draw()

        janela.update()


def cena_3_boa():
    janela = Window(800, 600)
    janela.set_title("Not a Hero!")

    mouse = Mouse()

    fundo = GameImage("imagens/cenas/fundo_fase3.jpg")
    texto = GameImage("imagens/cenas/texto_cena3_boa.png")
    botao_continuar = GameImage("imagens/menu_inicial/botao_continuar.png")

    botao_continuar.x = janela.width / 2 - 80
    botao_continuar.y = janela.height - 50

    while True:
        if mouse.is_button_pressed(1) and mouse.is_over_object(botao_continuar):
            fase4.iniciar_fase4()

        fundo.draw()
        texto.draw()
        botao_continuar.draw()

        janela.update()


def cena_3_ruim():
    janela = Window(800, 600)
    janela.set_title("Not a Hero!")

    mouse = Mouse()

    fundo = GameImage("imagens/cenas/fundo_fase3.jpg")
    texto = GameImage("imagens/cenas/texto_cena3_ruim.png")
    botao_continuar = GameImage("imagens/menu_inicial/botao_continuar.png")

    botao_continuar.x = janela.width / 2 - 80
    botao_continuar.y = janela.height - 50

    while True:
        if mouse.is_button_pressed(1) and mouse.is_over_object(botao_continuar):
            fase4.iniciar_fase4()

        fundo.draw()
        texto.draw()
        botao_continuar.draw()

        janela.update()




