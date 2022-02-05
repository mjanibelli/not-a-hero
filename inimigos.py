def movimentar_inimigo(inimigo, janela, velx, passos):
    inimigo.x += velx * janela.delta_time()

    if velx > 0:
        passos += velx * janela.delta_time()
    if velx < 0:
        passos += -velx * janela.delta_time()
    
    return passos


def mudar_sprite_inimigo(inimigo, sprite_novo):
    armz_x = inimigo.x 
    armz_y = inimigo.y

    inimigo = sprite_novo

    inimigo.x = armz_x
    inimigo.y = armz_y

    return inimigo


def direcionar_inimigo(inimigo, velx, sprite_direita, sprite_esquerda):
    if velx > 0:
        inimigo = mudar_sprite_inimigo(inimigo, sprite_direita)
    if velx < 0:
        inimigo = mudar_sprite_inimigo(inimigo, sprite_esquerda)
    
    return inimigo


def movimentar_chefao(chefe, jogador, janela, velx):
    chefe.x += -velx * janela.delta_time()
    chefe.y = jogador.y - 50

    