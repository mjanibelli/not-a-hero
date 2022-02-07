from PPlay.mouse import *
from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sound import *

import cenas

import fase1_plus


def tela_vitoria_fase1_boa():
    janela = Window(800, 600)
    janela.set_title("Not a Hero!")

    mouse = Mouse()

    fundo = GameImage("imagens/fase1/sky_cloud.jpg")
    texto = GameImage("imagens/fase1/texto_vitoria_bom.png")
    botao_continuar = GameImage("imagens/menu_inicial/botao_continuar.png")
    botao_continuar.x = janela.width / 2 - 80
    botao_continuar.y = janela.height - 100

    while True:
        if mouse.is_button_pressed(1) and mouse.is_over_object(botao_continuar):
            cenas.cena_1_boa()

        fundo.draw()
        botao_continuar.draw()
        texto.draw()
        janela.update()


def tela_vitoria_fase1_ruim():
    janela = Window(800, 600)
    janela.set_title("Not a Hero!")

    mouse = Mouse()

    fundo = GameImage("imagens/fase1/sky_cloud.jpg")
    texto = GameImage("imagens/fase1/texto_vitoria_ruim.png")
    botao_continuar = GameImage("imagens/menu_inicial/botao_continuar.png")
    botao_continuar.x = janela.width / 2 - 80
    botao_continuar.y = janela.height - 100

    while True:
        if mouse.is_button_pressed(1) and mouse.is_over_object(botao_continuar):
            cenas.cena_1_ruim()

        fundo.draw()
        botao_continuar.draw()
        texto.draw()
        janela.update()


def tela_vitoria_fase2_boa():
    janela = Window(800, 600)
    janela.set_title("Not a Hero!")

    mouse = Mouse()

    back1 = GameImage("imagens/fase2/background1.png")
    back2 = GameImage("imagens/fase2/background2.png")
    back3 = GameImage("imagens/fase2/background3.png")
    back4 = GameImage("imagens/fase2/background4.png")
    texto = GameImage("imagens/fase2/texto_vitoria_bom.png")
    botao_continuar = GameImage("imagens/menu_inicial/botao_continuar.png")
    botao_continuar.x = janela.width / 2 - 80
    botao_continuar.y = janela.height - 100

    while True:
        if mouse.is_button_pressed(1) and mouse.is_over_object(botao_continuar):
            cenas.cena_2_boa()

        back1.draw()
        back2.draw()
        back3.draw()
        back4.draw()
        botao_continuar.draw()
        texto.draw()
        janela.update()


def tela_vitoria_fase2_ruim():
    janela = Window(800, 600)
    janela.set_title("Not a Hero!")

    mouse = Mouse()

    back1 = GameImage("imagens/fase2/background1.png")
    back2 = GameImage("imagens/fase2/background2.png")
    back3 = GameImage("imagens/fase2/background3.png")
    back4 = GameImage("imagens/fase2/background4.png")
    texto = GameImage("imagens/fase2/texto_vitoria_ruim.png")
    botao_continuar = GameImage("imagens/menu_inicial/botao_continuar.png")
    botao_continuar.x = janela.width / 2 - 80
    botao_continuar.y = janela.height - 100

    while True:
        if mouse.is_button_pressed(1) and mouse.is_over_object(botao_continuar):
            cenas.cena_2_ruim()

        back1.draw()
        back2.draw()
        back3.draw()
        back4.draw()
        botao_continuar.draw()
        texto.draw()
        janela.update()


def tela_vitoria_fase3_boa():
    janela = Window(800, 600)
    janela.set_title("Not a Hero!")

    mouse = Mouse()

    fundo = GameImage("imagens/fase3/background.jpg")
    texto = GameImage("imagens/fase3/texto_vitoria_bom.png")
    botao_continuar = GameImage("imagens/menu_inicial/botao_continuar.png")
    botao_continuar.x = janela.width / 2 - 80
    botao_continuar.y = janela.height - 100

    while True:
        if mouse.is_button_pressed(1) and mouse.is_over_object(botao_continuar):
            cenas.cena_3_boa()

        fundo.draw()
        botao_continuar.draw()
        texto.draw()
        janela.update()


def tela_vitoria_fase3_ruim():
    janela = Window(800, 600)
    janela.set_title("Not a Hero!")

    mouse = Mouse()

    fundo = GameImage("imagens/fase3/background.jpg")
    texto = GameImage("imagens/fase3/texto_vitoria_ruim.png")
    botao_continuar = GameImage("imagens/menu_inicial/botao_continuar.png")
    botao_continuar.x = janela.width / 2 - 80
    botao_continuar.y = janela.height - 100

    while True:
        if mouse.is_button_pressed(1) and mouse.is_over_object(botao_continuar):
            cenas.cena_3_ruim()

        fundo.draw()
        botao_continuar.draw()
        texto.draw()
        janela.update()


def tela_jogo_nao_salvo():
    janela = Window(800, 600)
    janela.set_title("Not a Hero!")

    teclado = janela.get_keyboard()

    mouse = Mouse()

    fundo = GameImage("imagens/menu_inicial/fundo.png")
    aviso = GameImage("imagens/telas/aviso_save_nao_encontrado.png")
    botao_voltar = GameImage("imagens/telas/botao_voltar.png")
    
    aviso.x = 200
    aviso.y = 150

    botao_voltar.x = 325
    botao_voltar.y = janela.height - 110

    while True:
        # Entrada de Dados
        if teclado.key_pressed("esc"):
            break

        if mouse.is_button_pressed(1) and mouse.is_over_object(botao_voltar):
            break

        # Desenhos
        fundo.draw()
        aviso.draw()
        botao_voltar.draw()

        # Update
        janela.update()


def tela_creditos():
    janela = Window(800, 600)
    janela.set_title("Not a Hero!")

    teclado = janela.get_keyboard()

    mouse = Mouse()

    fundo = GameImage("imagens/menu_inicial/fundo.png")

    texto_creditos = GameImage("imagens/telas/texto_creditos.png")

    botao_voltar = GameImage("imagens/telas/botao_voltar.png")
    botao_voltar.x = janela.width / 2 - 80
    botao_voltar.y = 480

    while True:
        # Entrada de Dados
        if teclado.key_pressed("esc"):
            break

        if mouse.is_button_pressed(1) and mouse.is_over_object(botao_voltar):
            break

        # Desenhos
        fundo.draw()
        texto_creditos.draw()
        botao_voltar.draw()

        # Update
        janela.update()


def tela_creditos_final():
    janela = Window(800, 600)
    janela.set_title("Not a Hero!")

    mouse = Mouse()

    fundo = GameImage("imagens/menu_inicial/fundo.png")

    texto_creditos = GameImage("imagens/telas/texto_creditos.png")

    botao_sair = GameImage("imagens/menu_inicial/botao_sair.png")
    botao_sair.x = janela.width / 2 - 80
    botao_sair.y = 480

    while True:
        # Entrada de Dados
        if mouse.is_button_pressed(1) and mouse.is_over_object(botao_sair):
            janela.close()
            break

        # Desenhos
        fundo.draw()
        texto_creditos.draw()
        botao_sair.draw()

        # Update
        janela.update()


def tela_controles():
        janela = Window(800, 600)
        janela.set_title("Not a Hero!")

        teclado = janela.get_keyboard()

        mouse = Mouse()

        fundo = GameImage("imagens/menu_inicial/fundo.png")

        texto_creditos = GameImage("imagens/telas/texto_controles.png")

        botao_voltar = GameImage("imagens/telas/botao_voltar.png")
        botao_voltar.x = janela.width / 2 - 80
        botao_voltar.y = 480

        while True:
            # Entrada de Dados
            if teclado.key_pressed("esc"):
                break

            if mouse.is_button_pressed(1) and mouse.is_over_object(botao_voltar):
                break

            # Desenhos
            fundo.draw()
            texto_creditos.draw()
            botao_voltar.draw()

            # Update
            janela.update()


def tela_jogo_nao_fechado():
    janela = Window(800, 600)
    janela.set_title("Not a Hero!")

    teclado = janela.get_keyboard()

    mouse = Mouse()

    fundo = GameImage("imagens/menu_inicial/fundo.png")

    texto_aviso = GameImage("imagens/telas/texto_aviso_new_game_plus.png")

    botao_voltar = GameImage("imagens/telas/botao_voltar.png")
    botao_voltar.x = janela.width / 2 - 80
    botao_voltar.y = 480

    while True:
        # Entrada de Dados
        if teclado.key_pressed("esc"):
            break

        if mouse.is_button_pressed(1) and mouse.is_over_object(botao_voltar):
            break

        # Desenhos
        fundo.draw()
        texto_aviso.draw()
        botao_voltar.draw()

        # Update
        janela.update()


def tela_aviso_ngplus():
    janela = Window(800, 600)
    janela.set_title("Not a Hero!")

    mouse = Mouse()

    fundo = GameImage("imagens/menu_inicial/fundo.png")

    texto_aviso = GameImage("imagens/telas/aviso_ngplus.png")

    botao_continuar = GameImage("imagens/menu_inicial/botao_continuar.png")
    botao_continuar.x = janela.width / 2 - 80
    botao_continuar.y = 480

    while True:
    # Entrada de Dados
        if mouse.is_button_pressed(1) and mouse.is_over_object(botao_continuar):
            fase1_plus.iniciar_fase1()

        # Desenhos
        fundo.draw()
        texto_aviso.draw()
        botao_continuar.draw()

        # Update
        janela.update()


def tela_final_boa():
    janela = Window(800, 600)
    janela.set_title("Not a Hero!")

    mouse = Mouse()

    musica = Sound("musicas/musica_final.ogg")
    musica.set_volume(5)
    musica.set_repeat(True) 

    fundo = GameImage("imagens/cenas/fundo_final.jpg")
    texto = GameImage("imagens/cenas/texto_cena_final_boa.png")
    botao_finalizar_jogo = GameImage("imagens/menu_inicial/botao_finalizar_jogo.png")

    botao_finalizar_jogo.x = janela.width / 2 - 80
    botao_finalizar_jogo.y = janela.height - 50

    while True:
        musica.play()

        if mouse.is_button_pressed(1) and mouse.is_over_object(botao_finalizar_jogo):
            tela_creditos_final()

        fundo.draw()
        texto.draw()
        botao_finalizar_jogo.draw()

        janela.update()


def tela_final_ruim():
    janela = Window(800, 600)
    janela.set_title("Not a Hero!")

    mouse = Mouse()

    musica = Sound("musicas/musica_final.ogg")
    musica.set_volume(5)
    musica.set_repeat(True) 

    fundo = GameImage("imagens/cenas/fundo_inicio.jpg")
    texto = GameImage("imagens/cenas/texto_cena_final_ruim.png")
    botao_finalizar_jogo = GameImage("imagens/menu_inicial/botao_finalizar_jogo.png")

    botao_finalizar_jogo.x = janela.width / 2 - 80
    botao_finalizar_jogo.y = janela.height - 50

    while True:
        musica.play()

        if mouse.is_button_pressed(1) and mouse.is_over_object(botao_finalizar_jogo):
            tela_creditos_final()

        fundo.draw()
        texto.draw()
        botao_finalizar_jogo.draw()

        janela.update()


def tela_final_ngplus():
    janela = Window(800, 600)
    janela.set_title("Not a Hero!")

    mouse = Mouse()

    musica = Sound("musicas/musica_final.ogg")
    musica.set_volume(5)
    musica.set_repeat(True) 

    fundo = GameImage("imagens/menu_inicial/fundo.png")
    texto = GameImage("imagens/telas/texto_ngplus.png")
    botao_finalizar_jogo = GameImage("imagens/menu_inicial/botao_finalizar_jogo.png")

    botao_finalizar_jogo.x = janela.width / 2 - 80
    botao_finalizar_jogo.y = janela.height - 50

    while True:
        musica.play()

        if mouse.is_button_pressed(1) and mouse.is_over_object(botao_finalizar_jogo):
            tela_creditos_final()

        fundo.draw()
        texto.draw()
        botao_finalizar_jogo.draw()

        janela.update()