def carregar_final_bom():
    with open("arquivos_salvamento/final_bom", "r") as arquivo:
            final_bom = arquivo.read()

            return int(final_bom)


def carregar_final_ruim():
    with open("arquivos_salvamento/final_ruim", "r") as arquivo:
            final_ruim = arquivo.read()

            return int(final_ruim)