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


def iniciar_fase3():
    janela = Window(800, 600)
    janela.set_title("Not a Hero!")

    teclado = janela.get_keyboard()

    janela.update()

    musica = Sound("musicas/musica_fase3.ogg")
    musica.set_repeat(True)
    musica_boss = Sound("musicas/musica_bosses.ogg")
    musica.set_volume(5)
    musica_boss.set_volume(5)

    # Background
    back = GameImage("imagens/fase3/background.jpg")

    # Plataformas
    plataforma_1 = GameImage("imagens/fase3/pilar1.png")
    plataforma_1.y = janela.height - plataforma_1.height

    piso_plat_1 = GameImage("imagens/fase3/piso_pilar1.png")
    piso_plat_1.y = plataforma_1.y - piso_plat_1.height

    plataforma_2 = GameImage("imagens/fase3/pilar2.png")
    plataforma_2.x = plataforma_1.x + plataforma_1.width + 75
    plataforma_2.y = janela.height - plataforma_2.height + 15

    piso_plat_2 = GameImage("imagens/fase3/piso_pilar2.png")
    piso_plat_2.x = plataforma_2.x
    piso_plat_2.y = plataforma_2.y - piso_plat_2.height

    plataforma_3 = GameImage("imagens/fase3/pilar3.png")
    plataforma_3.x = plataforma_2.x + plataforma_2.width + 80
    plataforma_3.y = janela.height - plataforma_3.height + 190

    piso_plat_3 = GameImage("imagens/fase3/piso_pilar3.png")
    piso_plat_3.x = plataforma_3.x
    piso_plat_3.y = plataforma_3.y - piso_plat_3.height

    plataforma_4 = GameImage("imagens/fase3/pilar4.png")
    plataforma_4.x = plataforma_3.x + plataforma_3.width + 70
    plataforma_4.y = janela.height - plataforma_4.height 

    piso_plat_4 = GameImage("imagens/fase3/piso_pilar4.png")
    piso_plat_4.x = plataforma_4.x
    piso_plat_4.y = plataforma_4.y - piso_plat_4.height

    # Elementos do Cenário
    pedra = GameImage("imagens/fase1/rock_1.png")
    pedra.y = piso_plat_1.y - pedra.height
    
    arvore = GameImage("imagens/fase3/arvore.png")
    arvore.x = piso_plat_2.x + 10
    arvore.y = piso_plat_2.y - arvore.height

    tronco = GameImage("imagens/fase3/tronco.png")
    tronco.x = piso_plat_4.x + 20
    tronco.y = piso_plat_4.y - tronco.height

    # Jogador
    jogador = Animation("imagens/jogador/Idle.png", 8)
    jogador.set_sequence_time(0, 7, 200)
    jogador.y = piso_plat_1.y - 40

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

    escudo = GameImage("imagens/jogador/icone_escudo.png")
    escudo.y = 35

    escudo_ativo = True
    invulneravel = False
    cronometro_invulneravel = 0

    # Inimigos
    larva_de_fogo1 = Animation("imagens/fase3/larva_de_fogo.png", 9)
    larva_de_fogo1.set_sequence_time(0, 8, 100)
    larva_de_fogo1.x = piso_plat_2.x + 30
    larva_de_fogo1.y = piso_plat_2.y - larva_de_fogo1.height + 1

    larva_de_fogo1_atirando_dir = Animation("imagens/fase3/larva_de_fogo_atirando_dir.png", 16)
    larva_de_fogo1_atirando_dir.set_sequence_time(0, 15, 100)

    larva_de_fogo1_atirando_esq = Animation("imagens/fase3/larva_de_fogo_atirando_esq.png", 16)
    larva_de_fogo1_atirando_esq.set_sequence_time(0, 15, 100)

    larva_de_fogo2 = Animation("imagens/fase3/larva_de_fogo.png", 9)
    larva_de_fogo2.set_sequence_time(0, 8, 100)
    larva_de_fogo2.x = piso_plat_3.x + 30
    larva_de_fogo2.y = piso_plat_3.y - larva_de_fogo2.height + 1

    larva_de_fogo2_atirando_dir = Animation("imagens/fase3/larva_de_fogo_atirando_dir.png", 16)
    larva_de_fogo2_atirando_dir.set_sequence_time(0, 15, 100)

    larva_de_fogo2_atirando_esq = Animation("imagens/fase3/larva_de_fogo_atirando_esq.png", 16)
    larva_de_fogo2_atirando_esq.set_sequence_time(0, 15, 100)

    chefao = Animation("imagens/fase3/boss_andando.png", 4)
    chefao.set_sequence_time(0, 3, 100)
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

        if jogador.collided(piso_plat_1):
            no_chao = True
        
        if jogador.collided(piso_plat_2):
            no_chao = True
        
        if jogador.collided(piso_plat_3):
            no_chao = True

        if jogador.collided(piso_plat_4):
            no_chao = True

        # Mecânica do Escudo
        if escudo_ativo:
            if jogador.collided(larva_de_fogo1) or jogador.collided(larva_de_fogo2):
                escudo_ativo = False
                invulneravel = True
        
        if invulneravel:
            cronometro_invulneravel += janela.delta_time()

            if cronometro_invulneravel >= 2:
                invulneravel = False
                cronometro_invulneravel = 0
        
        if not escudo_ativo and not invulneravel:
            if jogador.collided(larva_de_fogo1) or jogador.collided(larva_de_fogo2):
                tentativas += 1
                jogador.x = 0
                jogador.y = piso_plat_1.y - 40
                escudo_ativo = True
            
                if chefe_vivo:
                    musica_boss.stop()
                    chefe_vivo = False
                    chefao.x = janela.width - chefao.width
                    chefao.y = 300
        # Fim da Mecânica do Escudo

        if jogador.y >= janela.height or jogador.collided(chefao):
            tentativas += 1
            jogador.x = 0
            jogador.y = piso_plat_1.y - 40
            escudo_ativo = True

            if chefe_vivo:
                musica_boss.stop()
                chefe_vivo = False
                chefao.x = janela.width - chefao.width
                chefao.y = 300
        
        if jogador.collided(tronco):
            musica.stop()
            chefe_vivo = True
        
        if not no_chao:
            jogador.y += 110 * janela.delta_time()
        
        if chefe_vivo and jogador.collided(pedra):
            musica_boss.stop()
            salvar.salvar_progresso("4")
            
            if tentativas < 10:
                qtd_finais_bons = carregar_finais.carregar_final_bom()
                qtd_finais_bons += 1
                salvar.salvar_final_bom(str(qtd_finais_bons))

                telas.tela_vitoria_fase3_boa()

            if tentativas >= 10:
                qtd_finais_ruins = carregar_finais.carregar_final_ruim()
                qtd_finais_ruins += 1
                salvar.salvar_final_ruim(str(qtd_finais_ruins))

                telas.tela_vitoria_fase3_ruim()
        
            # Movimentação Player
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
        if jogador.x <= larva_de_fogo1.x:
            larva_de_fogo1 = inimigos.mudar_sprite_inimigo(larva_de_fogo1, larva_de_fogo1_atirando_esq)
        if jogador.x > larva_de_fogo1.x:
            larva_de_fogo1 = inimigos.mudar_sprite_inimigo(larva_de_fogo1, larva_de_fogo1_atirando_dir)

        if jogador.x <= larva_de_fogo2.x:
            larva_de_fogo2 = inimigos.mudar_sprite_inimigo(larva_de_fogo2, larva_de_fogo2_atirando_esq)
        if jogador.x > larva_de_fogo2.x:
            larva_de_fogo2 = inimigos.mudar_sprite_inimigo(larva_de_fogo2, larva_de_fogo2_atirando_dir)

        if chefe_vivo:
            inimigos.movimentar_chefao(chefao, jogador, janela, 90)

        # Desenhos
        back.draw()
        janela.draw_text(f"Tentativas: {tentativas}", 0, 0, 24, color=(0, 0, 0), font_name="Bahnschrift")

        if escudo_ativo:
            escudo.draw()
        
        if invulneravel:
            janela.draw_text(f"Imune a dano!", 0, 35, 24, color=(0, 0, 0), font_name="Bahnschrift")

        plataforma_1.draw()
        piso_plat_1.draw()
        
        plataforma_2.draw()
        piso_plat_2.draw()
        
        plataforma_3.draw()
        piso_plat_3.draw()
        
        plataforma_4.draw()
        piso_plat_4.draw()
        
        pedra.draw()
        arvore.draw()
        tronco.draw()

        jogador.draw()
        larva_de_fogo1.draw()
        larva_de_fogo2.draw()

        if chefe_vivo:
            chefao.draw()

        # Update
        jogador.update()
        larva_de_fogo1.update()
        larva_de_fogo2.update()
        janela.update()

        if chefe_vivo:
            chefao.update()

