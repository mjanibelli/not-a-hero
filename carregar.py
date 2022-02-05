import fase1
import fase2
import fase3
import fase4
import telas


def carregar_progresso():
    try:
        with open("arquivos_salvamento/progresso_NAH", "r") as arquivo:
            progresso = arquivo.read()

            if progresso == '2':
                fase2.iniciar_fase2()
            elif progresso == '3':
                fase3.iniciar_fase3()
            elif progresso == '4':
                fase4.iniciar_fase4()
            else:
                fase1.iniciar_fase1()

    except FileNotFoundError:
        telas.tela_jogo_nao_salvo()
