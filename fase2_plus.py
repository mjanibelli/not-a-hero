from PPlay.animation import *
from PPlay.gameimage import *
from PPlay.window import *
from PPlay.sprite import *
from PPlay.sound import *

import player
import inimigos
import menus
import fase3_plus


def iniciar_fase2():
    janela = Window(800, 600)
    janela.set_title("Not a Hero!")
    
    teclado = janela.get_keyboard()

    janela.update()

    musica = Sound("musicas/musica_fase2.ogg")
    musica.set_repeat(True)
    musica_boss = Sound("musicas/musica_bosses.ogg")
    musica.set_volume(5)
    musica_boss.set_volume(5)

    # Background
    back1 = GameImage("imagens/fase2/background1.png")
    back2 = GameImage("imagens/fase2/background2.png")
    back3 = GameImage("imagens/fase2/background3.png")
    back4 = GameImage("imagens/fase2/background4.png")

    # Plataformas
    pilar_inicial = GameImage("imagens/fase2/pilar.png")
    pilar_inicial.y = janela.height - pilar_inicial.height

    chao_pilar_pedra = GameImage("imagens/fase2/chao_pilar_pedra.png")
    chao_pilar_pedra.y = pilar_inicial.y - chao_pilar_pedra.height

    plat_pedra1 = GameImage("imagens/fase2/plataforma_pedra.png")
    plat_pedra1.x = pilar_inicial.x + 140
    plat_pedra1.y = pilar_inicial.y + 100

    pilar_madeira1 = GameImage("imagens/fase2/pilar_madeira1.png")
    pilar_madeira1.x = plat_pedra1.x + 160
    pilar_madeira1.y = janela.height - pilar_madeira1.height

    plat_madeira1 = GameImage("imagens/fase2/plat_madeira.png")
    plat_madeira1.x = pilar_madeira1.x - 22
    plat_madeira1.y = pilar_madeira1.y - plat_madeira1.height

    plat_pedra2 = GameImage("imagens/fase2/plataforma_pedra.png")
    plat_pedra2.x = plat_madeira1.x + 150
    plat_pedra2.y = plat_madeira1.y - 50

    pilar_madeira2 = GameImage("imagens/fase2/pilar_madeira2.png")
    pilar_madeira2.x = plat_pedra2.x + 170
    pilar_madeira2.y = janela.height - pilar_madeira2.height + 50

    plat_madeira2 = GameImage("imagens/fase2/plat_madeira.png")
    plat_madeira2.x = pilar_madeira2.x - 22
    plat_madeira2.y = pilar_madeira2.y - plat_madeira2.height

    # Elementos do Cenário
    bau = GameImage("imagens/fase2/bau.png")
    bau.x = plat_madeira2.x + 22
    bau.y = plat_madeira2.y - bau.height

    pedra = GameImage("imagens/fase1/rock_1.png")
    pedra.x = chao_pilar_pedra.x
    pedra.y = chao_pilar_pedra.y - pedra.height

    # Jogador
    jogador = Animation("imagens/jogador/Idle.png", 8)
    jogador.set_sequence_time(0, 7, 200)
    jogador.y = chao_pilar_pedra.y - 40

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
    esqueleto = Animation("imagens/fase2/esqueleto_idle.png", 4)
    esqueleto.set_sequence_time(0, 3, 100)
    esqueleto.x = plat_pedra1.x 
    esqueleto.y = plat_pedra1.y - esqueleto.height
    velx_esqueleto = 20
    limite_esqueleto = 80
    passos_esqueleto = 0

    esqueleto_anda_direita = Animation("imagens/fase2/esqueleto_anda_direita.png", 4)
    esqueleto_anda_direita.set_sequence_time(0, 3, 100)

    esqueleto_anda_esquerda = Animation("imagens/fase2/esqueleto_anda_esquerda.png", 4)
    esqueleto_anda_esquerda.set_sequence_time(0, 3, 100)

    cogumelo = Animation("imagens/fase2/cogumelo_idle.png", 4)
    cogumelo.set_sequence_time(0, 3, 100)
    cogumelo.x = plat_pedra2.x
    cogumelo.y = plat_pedra2.y - cogumelo.height
    velx_cogumelo = 80
    limite_cogumelo = 80
    passos_cogumelo = 0

    cogumelo_anda_direita = Animation("imagens/fase2/cogumelo_anda_direita.png", 8)
    cogumelo_anda_direita.set_sequence_time(0, 7, 100)

    cogumelo_anda_esquerda = Animation("imagens/fase2/cogumelo_anda_esquerda.png", 8)
    cogumelo_anda_esquerda.set_sequence_time(0, 7, 100)

    chefao = Animation("imagens/fase2/boss_andando.png", 5)
    chefao.set_sequence_time(0, 4, 100)
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

        if jogador.collided(chao_pilar_pedra):
            no_chao = True
        
        if jogador.collided(plat_pedra1):
            no_chao = True
        
        if jogador.collided(plat_madeira1):
            no_chao = True

        if jogador.collided(plat_pedra2):
            no_chao = True
        
        if jogador.collided(plat_madeira2):
            no_chao = True
        
        if jogador.y >= janela.height or jogador.collided(esqueleto) or jogador.collided(cogumelo) or jogador.collided(chefao):
            if not chefe_vivo:
                musica.stop()
                menus.menu_inicial()

            if chefe_vivo:
                musica_boss.stop()
                menus.menu_inicial()
        
        if jogador.collided(bau):
            musica.stop()
            chefe_vivo = True
        
        if chefe_vivo and jogador.collided(pedra):
            musica_boss.stop()
            fase3_plus.iniciar_fase3()
                
        if not no_chao:
            jogador.y += 110 * janela.delta_time()
        
            # Movimentação do Player
        acao = player.movimentos(janela, teclado, jogador, no_chao, super_pulo=True)

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
        esqueleto = inimigos.direcionar_inimigo(esqueleto, velx_esqueleto, esqueleto_anda_direita, esqueleto_anda_esquerda)
        passos_esqueleto = inimigos.movimentar_inimigo(esqueleto, janela, velx_esqueleto, passos_esqueleto)

        if passos_esqueleto >= limite_esqueleto:
            passos_esqueleto = 0
            velx_esqueleto *= -1

        cogumelo = inimigos.direcionar_inimigo(cogumelo, velx_cogumelo, cogumelo_anda_direita, cogumelo_anda_esquerda)
        passos_cogumelo = inimigos.movimentar_inimigo(cogumelo, janela, velx_cogumelo, passos_cogumelo)

        if passos_cogumelo >= limite_cogumelo:
            passos_cogumelo = 0
            velx_cogumelo *= -1
        
        if chefe_vivo:
            inimigos.movimentar_chefao(chefao, jogador, janela, 100)

        # Desenhos
        back1.draw()
        back2.draw()
        back3.draw()
        back4.draw()

        chao_pilar_pedra.draw()
        pilar_inicial.draw()
        plat_madeira1.draw()
        pilar_madeira1.draw()
        plat_pedra1.draw()
        plat_pedra2.draw()
        plat_madeira2.draw()
        pilar_madeira2.draw()

        bau.draw()
        pedra.draw()

        jogador.draw()
        esqueleto.draw()
        cogumelo.draw()

        if chefe_vivo:
            chefao.draw()

        # Update
        jogador.update()
        esqueleto.update()
        cogumelo.update()
        janela.update()

        if chefe_vivo:
            chefao.update()