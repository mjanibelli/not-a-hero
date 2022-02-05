from PPlay.animation import *
from PPlay.gameimage import *
from PPlay.window import *
from PPlay.sprite import *
from PPlay.sound import *

import player
import inimigos
import telas
import menus
import salvar
import carregar_finais


def iniciar_fase4(): 
    janela = Window(800, 600)
    janela.set_title("Not a Hero!")

    teclado = janela.get_keyboard()

    janela.update()

    musica = Sound("musicas/musica_menu.ogg")
    musica.set_repeat(True)
    musica_boss = Sound("musicas/musica_fase4.ogg")
    musica.set_volume(5)
    musica_boss.set_volume(5)

    # Background
    back = GameImage("imagens/fase4/background.jpg")

    # Plataformas
    plataforma1 = GameImage("imagens/fase4/plataforma1.png")
    plataforma1.y = janela.height - plataforma1.height + 180

    chao_plat1 = GameImage("imagens/fase4/chao_plat1.png")
    chao_plat1.y = plataforma1.y - chao_plat1.height

    plataforma2 = GameImage("imagens/fase4/plataforma2.png")
    plataforma2.x = plataforma1.x + plataforma1.width + 60
    plataforma2.y = janela.height - plataforma2.height

    chao_plat2 = GameImage("imagens/fase4/chao_plat2.png")
    chao_plat2.x = plataforma2.x
    chao_plat2.y = plataforma2.y - chao_plat2.height

    plataforma3 = GameImage("imagens/fase4/plataforma3.png")
    plataforma3.x = plataforma2.x + plataforma2.width + 65
    plataforma3.y = janela.height - plataforma3.height

    chao_plat3 = GameImage("imagens/fase4/chao_plat3.png")
    chao_plat3.x = plataforma3.x
    chao_plat3.y = plataforma3.y - chao_plat3.height

    plataforma4 = GameImage("imagens/fase4/plataforma4.png")
    plataforma4.x = janela.width - plataforma4.width
    plataforma4.y = janela.height - plataforma4.height

    # Jogador
    jogador = Animation("imagens/jogador/heroi_idle.png", 8)
    jogador.set_sequence_time(0, 7, 200)
    jogador.y = chao_plat1.y - 40
    tentativas = 0

    jogador_parado = Animation("imagens/jogador/heroi_idle.png", 8)
    jogador_parado.set_sequence_time(0, 7, 200)

    jogador_corre_direita = Animation("imagens/jogador/heroi_correndo_dir.png", 10)
    jogador_corre_direita.set_sequence_time(0, 9, 120)

    jogador_corre_esq = Animation("imagens/jogador/heroi_correndo_esq.png", 10)
    jogador_corre_esq.set_sequence_time(0, 9, 120)

    jogador_pulo_dir = Animation("imagens/jogador/heroi_pulando_dir.png", 4)
    jogador_pulo_dir.set_sequence_time(0, 3, 100)

    jogador_pulo_esq = Animation("imagens/jogador/heroi_pulando_esq.png", 4)
    jogador_pulo_esq.set_sequence_time(0, 3, 100)

    jogador_ataque_dir = Animation("imagens/jogador/heroi_ataque_dir.png", 6)
    jogador_ataque_dir.set_sequence_time(0, 5, 70)

    jogador_ataque_esq = Animation("imagens/jogador/heroi_ataque_esq.png", 6)
    jogador_ataque_esq.set_sequence_time(0, 5, 70)

    escudo = GameImage("imagens/jogador/icone_escudo.png")
    escudo.y = 35

    escudo_ativo = True
    invulneravel = False
    cronometro_invulneravel = 0

    # Inimigos
    orc = Animation("imagens/fase1/orc_idle.png", 4)
    orc.set_sequence_time(0, 3, 100)
    orc.x = chao_plat1.x + 150
    orc.y = chao_plat1.y - 40
    velx_orc = -20
    limite_orc = 80
    passos_orc = 0
    orc_vivo = True

    orc_anda_direita = Animation("imagens/fase1/orc_run_dir.png", 10)
    orc_anda_direita.set_sequence_time(0, 9, 100)

    orc_anda_esquerda = Animation("imagens/fase1/orc_run_esq.png", 10)
    orc_anda_esquerda.set_sequence_time(0, 9, 100)

    larva_de_fogo = Animation("imagens/fase3/larva_de_fogo.png", 9)
    larva_de_fogo.set_sequence_time(0, 8, 100)
    larva_de_fogo.x = chao_plat2.x + 30
    larva_de_fogo.y = chao_plat2.y - larva_de_fogo.height - 8
    larva_viva = True

    larva_de_fogo_atirando_dir = Animation("imagens/fase3/larva_de_fogo_atirando_dir.png", 16)
    larva_de_fogo_atirando_dir.set_sequence_time(0, 15, 100)

    larva_de_fogo_atirando_esq = Animation("imagens/fase3/larva_de_fogo_atirando_esq.png", 16)
    larva_de_fogo_atirando_esq.set_sequence_time(0, 15, 100)

    esqueleto = Animation("imagens/fase2/esqueleto_idle.png", 4)
    esqueleto.set_sequence_time(0, 3, 100)
    esqueleto.x = chao_plat3.x 
    esqueleto.y = chao_plat3.y - esqueleto.height
    velx_esqueleto = 20
    limite_esqueleto = 80
    passos_esqueleto = 0
    esqueleto_vivo = True

    esqueleto_anda_direita = Animation("imagens/fase2/esqueleto_anda_direita.png", 4)
    esqueleto_anda_direita.set_sequence_time(0, 3, 100)

    esqueleto_anda_esquerda = Animation("imagens/fase2/esqueleto_anda_esquerda.png", 4)
    esqueleto_anda_esquerda.set_sequence_time(0, 3, 100)

    chefao = Animation("imagens/fase4/vilao_idle_esq.png", 8)
    chefao.set_sequence_time(0, 7, 100)
    chefao.x = janela.width - chefao.width
    chefao.y = plataforma4.y - chefao.height
    batalha_final = False
    cronometro_tiros = 1
    tiros = []

    chefao_direita = Animation("imagens/fase4/vilao_idle_dir.png", 8)
    chefao_direita.set_sequence_time(0, 7, 100)

    janela.update()

    while True:
        no_chao = False

        if not batalha_final:
            musica.play()
        
        # Entrada de Dados
        if teclado.key_pressed("esc"):
            if batalha_final:
                musica_boss.stop()
            if not batalha_final:
                musica.stop()
            menus.menu_inicial()

        if jogador.collided(chao_plat1):
            no_chao = True
        
        if jogador.collided(chao_plat2):
            no_chao = True
        
        if jogador.collided(chao_plat3):
            no_chao = True
        
        if jogador.collided(plataforma4):
            no_chao = True

        if jogador.collided(chefao):
            batalha_final = True
            
        if not no_chao:
            jogador.y += 110 * janela.delta_time()
        
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
        
        if acao == 6:
            jogador = player.mudar_sprite(jogador, jogador_ataque_dir)
        
        if acao == 7:
            jogador = player.mudar_sprite(jogador, jogador_ataque_esq)
        
            # Movimentação Inimigos
        if orc_vivo:
            orc = inimigos.direcionar_inimigo(orc, velx_orc, orc_anda_direita, orc_anda_esquerda)
            passos_orc = inimigos.movimentar_inimigo(orc, janela, velx_orc, passos_orc)

            if passos_orc >= limite_orc:
                passos_orc = 0
                velx_orc *= -1
        
        if esqueleto_vivo:
            esqueleto = inimigos.direcionar_inimigo(esqueleto, velx_esqueleto, esqueleto_anda_direita, esqueleto_anda_esquerda)
            passos_esqueleto = inimigos.movimentar_inimigo(esqueleto, janela, velx_esqueleto, passos_esqueleto)

            if passos_esqueleto >= limite_esqueleto:
                passos_esqueleto = 0
                velx_esqueleto *= -1
        
        if larva_viva:
            if jogador.x <= larva_de_fogo.x:
                larva_de_fogo = inimigos.mudar_sprite_inimigo(larva_de_fogo, larva_de_fogo_atirando_esq)
            if jogador.x > larva_de_fogo.x:
                larva_de_fogo = inimigos.mudar_sprite_inimigo(larva_de_fogo, larva_de_fogo_atirando_dir)

            # Mecânica do Escudo
        if escudo_ativo and acao < 6:
            if jogador.collided(orc) or jogador.collided(larva_de_fogo) or jogador.collided(esqueleto):
                escudo_ativo = False
                invulneravel = True
        
        if invulneravel:
            cronometro_invulneravel += janela.delta_time()

            if cronometro_invulneravel >= 2:
                invulneravel = False
                cronometro_invulneravel = 0
        
        if not escudo_ativo and not invulneravel:
            if jogador.collided(orc) or jogador.collided(larva_de_fogo) or jogador.collided(esqueleto):
                if batalha_final:
                    tentativas += 1
                    jogador.x = plataforma4.x + 50
                    jogador.y = plataforma4.y - 40
                    escudo_ativo = True
                
                if not batalha_final:
                    tentativas += 1
                    jogador.x = 0
                    jogador.y = chao_plat1.y - 40
                    escudo_ativo = True
            # Fim da Mecânica do Escudo
        
        if jogador.y >= janela.height:
            if batalha_final:
                tentativas += 1
                jogador.x = plataforma4.x + 50
                jogador.y = plataforma4.y - 40
                escudo_ativo = True

            if not batalha_final:
                tentativas += 1
                jogador.x = 0
                jogador.y = chao_plat1.y - 40
                escudo_ativo = True

            # Mecânica da Espada:
        if (acao == 6 or acao == 7) and jogador.collided(orc):
            orc.x = 0
            orc.y = 0
            orc_vivo = False
        
        if (acao == 6 or acao == 7) and jogador.collided(larva_de_fogo):
            larva_de_fogo.x = 0
            larva_de_fogo.y = 0
            larva_viva = False
        
        if (acao == 6 or acao == 7) and jogador.collided(esqueleto):
            esqueleto.x = 0
            esqueleto.y = 0
            esqueleto_vivo = False
            # Fim da Mecânica da Espada.
        
            # Batalha Final
        if batalha_final:
            musica.stop()
            musica_boss.play()

            chefao.x = 0
            chefao.y = chao_plat1.y - chefao.height
            chefao = inimigos.mudar_sprite_inimigo(chefao, chefao_direita)

            cronometro_tiros += janela.delta_time()

            if cronometro_tiros >= 0.75:
                projetil_chefao = Animation("imagens/fase4/projetil_vilao.png", 6)
                projetil_chefao.set_sequence_time(0, 5, 100)
                projetil_chefao.x = chefao.x 
                projetil_chefao.y = jogador.y

                tiros.append(projetil_chefao)
                cronometro_tiros = 0

            for tiro in tiros:
                tiro.x += 550 * janela.delta_time()

                if tiro.collided(jogador):
                    tiros.remove(tiro)

                    if escudo_ativo:
                        escudo_ativo = False
                        invulneravel = True

                    if not escudo_ativo and not invulneravel:
                        tentativas += 1
                        jogador.x = plataforma4.x + 50
                        jogador.y = plataforma4.y - 40
                        escudo_ativo = True
                    
                if tiro.x >= janela.width:
                    tiros.remove(tiro)
                
                if jogador.collided(chefao) and (acao == 6 or acao == 7):
                    musica_boss.stop()

                    if tentativas < 10:
                        qtd_finais_bons = carregar_finais.carregar_final_bom()
                        qtd_finais_bons += 1
                        salvar.salvar_final_bom(str(qtd_finais_bons))

                    if tentativas >= 10:
                        qtd_finais_ruins = carregar_finais.carregar_final_ruim()
                        qtd_finais_ruins += 1
                        salvar.salvar_final_ruim(str(qtd_finais_ruins))
                    
                    qtd_finais_bons = carregar_finais.carregar_final_bom()
                    qtd_finais_ruins = carregar_finais.carregar_final_ruim()

                    if qtd_finais_bons > qtd_finais_ruins:
                        telas.tela_final_boa()
                        
                    if qtd_finais_bons <= qtd_finais_ruins:
                        telas.tela_final_ruim()
                    
            # Fim da Batalha Final

        # Desenhos
        back.draw()
        janela.draw_text(f"Tentativas: {tentativas}", 0, 0, 24, color=(255, 255, 255), font_name="Bahnschrift")

        if escudo_ativo:
            escudo.draw()
        
        if invulneravel:
            janela.draw_text(f"Imune a dano!", 0, 35, 24, color=(0, 0, 0), font_name="Bahnschrift")

        plataforma1.draw()
        chao_plat1.draw()
        plataforma2.draw()
        chao_plat2.draw()
        plataforma3.draw()
        chao_plat3.draw()
        plataforma4.draw()

        jogador.draw()

        if orc_vivo:
            orc.draw()
        if larva_viva:
            larva_de_fogo.draw()
        if esqueleto_vivo:
            esqueleto.draw()

        chefao.draw()
        
        if batalha_final:
            for tiro in tiros:
                tiro.draw()

        # Updates
        if batalha_final:
            for tiro in tiros:
                tiro.update()

        jogador.update()
        chefao.update()
        orc.update()
        larva_de_fogo.update()
        esqueleto.update()
        janela.update()


