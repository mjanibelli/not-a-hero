from PPlay.mouse import *
from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sound import *

import carregar
import telas
import cenas


def menu_inicial():
    janela = Window(800, 600)
    janela.set_title("Not a Hero!")

    janela.update()

    mouse = Mouse()

    titulo = GameImage("imagens/menu_inicial/titulo.png")
    titulo.x = 180
    titulo.y = 10

    fundo = GameImage("imagens/menu_inicial/fundo.png")

    botao_novo_jogo = GameImage("imagens/menu_inicial/botao_novo_jogo.png")
    botao_continuar = GameImage("imagens/menu_inicial/botao_continuar.png")
    botao_controles = GameImage("imagens/menu_inicial/botao_controles.png")
    botao_creditos = GameImage("imagens/menu_inicial/botao_creditos.png")
    botao_sair = GameImage("imagens/menu_inicial/botao_sair.png")

    botao_novo_jogo.x = janela.width / 2 - 80
    botao_novo_jogo.y = 220

    botao_continuar.x = botao_novo_jogo.x
    botao_continuar.y = botao_novo_jogo.y + 55

    botao_controles.x = botao_novo_jogo.x
    botao_controles.y = botao_continuar.y + 55

    botao_creditos.x = botao_novo_jogo.x
    botao_creditos.y = botao_controles.y + 55

    botao_sair.x = botao_novo_jogo.x
    botao_sair.y = botao_creditos.y + 55

    musica = Sound("musicas/musica_menu.ogg")
    musica.set_repeat(True)
    musica.set_volume(5)

    janela.update()

    while True:
        # Música
        musica.play()

        # Entrada de dados
        if mouse.is_button_pressed(1) and mouse.is_over_object(botao_novo_jogo):
            musica.stop()
            cenas.cena_inicial()
        
        if mouse.is_button_pressed(1) and mouse.is_over_object(botao_continuar):
            musica.stop()
            carregar.carregar_progresso()
        
        if mouse.is_button_pressed(1) and mouse.is_over_object(botao_controles):
            telas.tela_controles()
        
        if mouse.is_button_pressed(1) and mouse.is_over_object(botao_creditos):
            telas.tela_creditos()
        
        if mouse.is_button_pressed(1) and mouse.is_over_object(botao_sair):
            janela.close()
            break
            
        # Desenhos
        fundo.draw()
        titulo.draw()
        botao_novo_jogo.draw()
        botao_continuar.draw()
        botao_controles.draw()
        botao_creditos.draw()
        botao_sair.draw()

        # Update
        janela.update()