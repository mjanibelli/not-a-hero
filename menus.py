from PPlay.mouse import *
from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sound import *

import carregar
import telas
import cenas


def menu_inicial():
    try:
        with open("arquivos_salvamento/jogo_finalizado", "r") as arquivo:
            jogo_fechado = arquivo.read()
    except FileNotFoundError:
        jogo_fechado = 0 

    janela = Window(800, 600)
    janela.set_title("Not a Hero!")

    janela.update()

    mouse = Mouse()
    click = True
    cronometro_click = 0

    titulo = GameImage("imagens/menu_inicial/titulo.png")
    titulo.x = 180
    titulo.y = 10

    fundo = GameImage("imagens/menu_inicial/fundo.png")

    botao_novo_jogo = GameImage("imagens/menu_inicial/botao_novo_jogo.png")
    botao_novo_jogo_plus = GameImage("imagens/menu_inicial/botao_novo_jogo_plus.png")
    botao_continuar = GameImage("imagens/menu_inicial/botao_continuar.png")
    botao_controles = GameImage("imagens/menu_inicial/botao_controles.png")
    botao_creditos = GameImage("imagens/menu_inicial/botao_creditos.png")
    botao_sair = GameImage("imagens/menu_inicial/botao_sair.png")

    botao_novo_jogo.x = janela.width / 2 - 80
    botao_novo_jogo.y = 180

    botao_novo_jogo_plus.x = botao_novo_jogo.x
    botao_novo_jogo_plus.y = botao_novo_jogo.y + 60

    botao_continuar.x = botao_novo_jogo.x
    botao_continuar.y = botao_novo_jogo_plus.y + 60

    botao_controles.x = botao_novo_jogo.x
    botao_controles.y = botao_continuar.y + 60

    botao_creditos.x = botao_novo_jogo.x
    botao_creditos.y = botao_controles.y + 60

    botao_sair.x = botao_novo_jogo.x
    botao_sair.y = botao_creditos.y + 60

    musica = Sound("musicas/musica_menu.ogg")
    musica.set_repeat(True)
    musica.set_volume(5)

    janela.update()

    while True:

        # Segurar Clicks em sequência
        if click is False:
            cronometro_click += janela.delta_time()

            if cronometro_click >= 0.1:
                click = True
                cronometro_click = 0
        
        # Música
        musica.play()

        # Entrada de dados
        if mouse.is_button_pressed(1) and mouse.is_over_object(botao_novo_jogo) and click:
            musica.stop()
            click = False
            cenas.cena_inicial()
        
        if mouse.is_button_pressed(1) and mouse.is_over_object(botao_novo_jogo_plus) and click:
            if int(jogo_fechado) == 0:
                click = False
                telas.tela_jogo_nao_fechado()
                janela.update()
            
            if int(jogo_fechado) == 1:
                musica.stop()
                telas.tela_aviso_ngplus()
        
        if mouse.is_button_pressed(1) and mouse.is_over_object(botao_continuar) and click:
            musica.stop()
            click = False
            carregar.carregar_progresso()
            janela.update()
        
        if mouse.is_button_pressed(1) and mouse.is_over_object(botao_controles) and click:
            click = False
            telas.tela_controles()
            janela.update()
        
        if mouse.is_button_pressed(1) and mouse.is_over_object(botao_creditos) and click:
            click = False
            telas.tela_creditos()
            janela.update()
        
        if mouse.is_button_pressed(1) and mouse.is_over_object(botao_sair) and click:
            click = False
            janela.close()
            break
            
        # Desenhos
        fundo.draw()
        titulo.draw()
        botao_novo_jogo.draw()
        botao_novo_jogo_plus.draw()
        botao_continuar.draw()
        botao_controles.draw()
        botao_creditos.draw()
        botao_sair.draw()

        # Update
        janela.update()