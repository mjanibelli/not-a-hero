from PPlay.animation import *
from PPlay.gameimage import *
from PPlay.window import *
from PPlay.sprite import *
from PPlay.sound import *

import salvar
import player
import inimigos
import telas
import menus
import carregar_finais


def iniciar_fase1():
    salvar.salvar_progresso("1")
    salvar.salvar_final_bom("0")
    salvar.salvar_final_ruim("0")
    
    janela = Window(800, 600)
    janela.set_title("Not a Hero!")
    teclado = janela.get_keyboard()

    janela.update()

    musica = Sound("musicas/musica_fase1.ogg")
    musica.set_repeat(True)
    musica_boss = Sound("musicas/musica_bosses.ogg")
    musica.set_volume(5)
    musica_boss.set_volume(5)

    # Background
    ceu = GameImage("imagens/fase1/sky_cloud.jpg")

    floresta = GameImage("imagens/fase1/pine2.png")
    floresta.y = janela.height - floresta.height

    # Plataformas
    chao_1 = GameImage("imagens/fase1/chao1.png")
    chao_1.y = janela.height - chao_1.height

    piso_1 = GameImage("imagens/fase1/piso_chao1.png")
    piso_1.y = chao_1.y - piso_1.height

    chao_2 = GameImage("imagens/fase1/chao2.png")
    chao_2.x = chao_1.x + chao_1.width + 80
    chao_2.y = janela.height - 80

    piso_2 = GameImage("imagens/fase1/piso_chao2.png")
    piso_2.x = chao_2.x
    piso_2.y = chao_2.y - piso_2.height

    chao_3 = GameImage("imagens/fase1/chao3.png")
    chao_3.x = chao_2.x + chao_2.width + 85
    chao_3.y = chao_1.y

    piso_3 = GameImage("imagens/fase1/piso_chao3.png")
    piso_3.x = chao_3.x
    piso_3.y = chao_3.y - piso_3.height

    # Elementos do cenário
    arvore1 = GameImage("imagens/fase1/tree.png")
    arvore1.x = 75
    arvore1.y = piso_1.y - arvore1.height

    arvore2 = GameImage("imagens/fase1/tree.png")
    arvore2.x = piso_2.x + 20
    arvore2.y = piso_2.y - arvore2.height

    arbusto = GameImage("imagens/fase1/bush_1.png")
    arbusto.x = piso_3.x + 110
    arbusto.y = piso_3.y - arbusto.height

    pedra = GameImage("imagens/fase1/rock_1.png")
    pedra.x = piso_1.x
    pedra.y = piso_1.y - pedra.height

    # Jogador
    jogador = Animation("imagens/jogador/Idle.png", 8)
    jogador.set_sequence_time(0, 7, 200)
    jogador.y = piso_1.y - 40
    tentativas = 0

    jogador_parado = Animation("imagens/jogador/Idle.png", 8)
    jogador_parado.set_sequence_time(0, 7, 200)

    jogador_corre_direita = Animation("imagens/jogador/Run_dir.png", 8)
    jogador_corre_direita.set_sequence_time(0, 7, 120)

    jogador_corre_esq = Animation("imagens/jogador/Run_esq.png", 8)
    jogador_corre_esq.set_sequence_time(0, 7, 120)

    jogador_pulo_dir = Animation("imagens/jogador/Jump_dir.png", 2)
    jogador_pulo_dir.set_sequence_time(0, 1, 1)

    jogador_pulo_esq = Animation("imagens/jogador/Jump_esq.png", 2)
    jogador_pulo_esq.set_sequence_time(0, 1, 1)

    # Inimigos
    goblin1 = Animation("imagens/fase1/goblin_idle.png", 4)
    goblin1.set_sequence_time(0, 3, 100)
    goblin1.x = piso_1.x + 80
    goblin1.y = piso_1.y - 38
    velx_goblin1 = 60
    limite_goblin1 = 130
    passos_goblin1 = 0

    goblin1_anda_direita = Animation("imagens/fase1/goblin_run_dir.png", 8)
    goblin1_anda_direita.set_sequence_time(0, 7, 100)

    goblin1_anda_esq = Animation("imagens/fase1/goblin_run_esq.png", 8)
    goblin1_anda_esq.set_sequence_time(0, 7, 100)

    goblin2 = Animation("imagens/fase1/goblin_idle.png", 4)
    goblin2.set_sequence_time(0, 3, 100)
    goblin2.x = piso_3.x
    goblin2.y = piso_3.y - 38
    velx_goblin2 = 60
    limite_goblin2 = 200
    passos_goblin2 = 0

    goblin2_anda_direita = Animation("imagens/fase1/goblin_run_dir.png", 8)
    goblin2_anda_direita.set_sequence_time(0, 7, 100)

    goblin2_anda_esq = Animation("imagens/fase1/goblin_run_esq.png", 8)
    goblin2_anda_esq.set_sequence_time(0, 7, 100)

    orc = Animation("imagens/fase1/orc_idle.png", 4)
    orc.set_sequence_time(0, 3, 100)
    orc.x = piso_2.x
    orc.y = piso_2.y - 40
    velx_orc = 20
    limite_orc = 80
    passos_orc = 0

    orc_anda_direita = Animation("imagens/fase1/orc_run_dir.png", 10)
    orc_anda_direita.set_sequence_time(0, 9, 100)

    orc_anda_esquerda = Animation("imagens/fase1/orc_run_esq.png", 10)
    orc_anda_esquerda.set_sequence_time(0, 9, 100)

    chefao = Animation("imagens/fase1/boss_andando.png", 8)
    chefao.set_sequence_time(0, 7, 100)
    chefao.x = janela.width - chefao.width
    chefao.y = 300
    chefe_vivo = False

    janela.update()

    while True:
        no_chao = False

        if not chefe_vivo:
            musica.play()
        
        if chefe_vivo:
            musica_boss.play()

        # Entrada de Dados
        if teclado.key_pressed("esc"):
            if chefe_vivo:
                musica_boss.stop()
            if not chefe_vivo:
                musica.stop()
            menus.menu_inicial()

        if jogador.collided(piso_1):
            no_chao = True
        
        if jogador.collided(piso_2):
            no_chao = True
        
        if jogador.collided(piso_3):
            no_chao = True

        if jogador.y >= janela.height or jogador.collided(goblin1) or jogador.collided(goblin2) or jogador.collided(orc) or jogador.collided(chefao):
            tentativas += 1
            jogador.x = 0
            jogador.y = piso_1.y - 40

            if chefe_vivo:
                musica_boss.stop()
                chefe_vivo = False
                chefao.x = janela.width - chefao.width
                chefao.y = 300
            
        if jogador.collided(arbusto):
            musica.stop()
            chefe_vivo = True

        if not no_chao:
            jogador.y += 95 * janela.delta_time()
        
        if chefe_vivo and jogador.collided(pedra):
            musica_boss.stop()
            salvar.salvar_progresso("2")

            if tentativas < 10:
                qtd_finais_bons = carregar_finais.carregar_final_bom()
                qtd_finais_bons += 1
                salvar.salvar_final_bom(str(qtd_finais_bons))

                telas.tela_vitoria_fase1_boa()

            if tentativas >= 10:
                qtd_finais_ruins = carregar_finais.carregar_final_ruim()
                qtd_finais_ruins += 1
                salvar.salvar_final_ruim(str(qtd_finais_ruins))

                telas.tela_vitoria_fase1_ruim()
            
            # Movimentação Player
        acao = player.movimentos(janela, teclado, jogador, no_chao)

        if acao == 1:  # Jogador Parado
            jogador = player.mudar_sprite(jogador, jogador_parado)

        if acao == 2:  # Jogadr Correndo para direita
            jogador = player.mudar_sprite(jogador, jogador_corre_direita)

        if acao == 3:  # Jogador Correndo para esquerda
            jogador = player.mudar_sprite(jogador, jogador_corre_esq)
        
        if acao == 4: # Jogador Caindo para esquerda
            jogador = player.mudar_sprite(jogador, jogador_pulo_esq)
        
        if acao == 5:  # Jogador Caindo para direita
            jogador = player.mudar_sprite(jogador, jogador_pulo_dir)

            # Movimentação dos Inimigos
        goblin1 = inimigos.direcionar_inimigo(goblin1, velx_goblin1, goblin1_anda_direita, goblin1_anda_esq)
        passos_goblin1 = inimigos.movimentar_inimigo(goblin1, janela, velx_goblin1, passos_goblin1)

        if passos_goblin1 >= limite_goblin1:
            passos_goblin1 = 0
            velx_goblin1 *= -1
        
        goblin2 = inimigos.direcionar_inimigo(goblin2, velx_goblin2, goblin2_anda_direita, goblin2_anda_esq)
        passos_goblin2 = inimigos.movimentar_inimigo(goblin2, janela, velx_goblin2, passos_goblin2)

        if passos_goblin2 >= limite_goblin2:
            passos_goblin2 = 0
            velx_goblin2 *= -1

        orc = inimigos.direcionar_inimigo(orc, velx_orc, orc_anda_direita, orc_anda_esquerda)
        passos_orc = inimigos.movimentar_inimigo(orc, janela, velx_orc, passos_orc)

        if passos_orc >= limite_orc:
            passos_orc = 0
            velx_orc *= -1
        
        if chefe_vivo:
            inimigos.movimentar_chefao(chefao, jogador, janela, 100)

        # Desenhos
        ceu.draw()
        floresta.draw()
        janela.draw_text(f"Tentativas: {tentativas}", 0, 0, 24, color=(0, 0, 0), font_name="Bahnschrift")

        chao_1.draw()
        piso_1.draw()
        chao_2.draw()
        piso_2.draw()
        chao_3.draw()
        piso_3.draw()

        arvore1.draw()
        arvore2.draw()
        arbusto.draw()
        pedra.draw()

        goblin1.draw()
        goblin2.draw()
        orc.draw()
        jogador.draw()

        if chefe_vivo:
            chefao.draw()

        # Update
        goblin1.update()
        goblin2.update()
        orc.update()
        jogador.update()
        janela.update()

        if chefe_vivo:
            chefao.update()

