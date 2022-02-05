from PPlay.animation import *


def movimentos(janela, teclado, jogador, no_chao, super_pulo=False) -> int:
    jogador_velX = 100

    if not super_pulo:
        jogador_velY = 105
    if super_pulo:
        jogador_velY = 165

    parado = True
    direita = False
    esquerda = False

    # Caminhada para direita
    if (teclado.key_pressed("right") or teclado.key_pressed("d")) and jogador.x + jogador.width  < janela.width:  # O resto da condicional é para avaliar as bordas da janela.
        jogador.x += jogador_velX * janela.delta_time()

        direita = True

        if no_chao:
            parado = False
    
    # Caminhada para esquerda
    if (teclado.key_pressed("left") or teclado.key_pressed("a")) and jogador.x > 0:  # O resto da condicional é para avaliar as bordas da janela.
        jogador.x -= jogador_velX * janela.delta_time()

        esquerda = True

        if no_chao:
            parado = False
    
    if parado:
        movimento = 1  # Jogador Parado

    if not parado:
        if direita:
            movimento = 2  # Andando para direita
        
        if esquerda:
            movimento = 3  # Andando para esquerda

    # Pulo
    if no_chao:
        if teclado.key_pressed("up") or teclado.key_pressed("w"):
            jogador.y -= jogador_velY
        
        # Ataque
        if teclado.key_pressed("space") or teclado.key_pressed("z"):
            movimento = 6  # Jogador atacando para direta.
        
        if (teclado.key_pressed("a") or teclado.key_pressed("left")) and (teclado.key_pressed("space") or teclado.key_pressed("z")):
            movimento = 7  # Jogador atacando para esquerda.

    # Queda
    if not no_chao:
        if esquerda:
            movimento = 4  # Caindo para esquerda
        
        else:
            movimento = 5  # Caindo para direita
    
        
    return movimento


def mudar_sprite(jogador, sprite_novo) -> Animation:
    armz_x = jogador.x 
    armz_y = jogador.y

    jogador = sprite_novo

    jogador.x = armz_x
    jogador.y = armz_y

    return jogador




