def salvar_progresso(progresso):
    with open("arquivos_salvamento/progresso_NAH", "w") as arquivo:
        arquivo.write(progresso)


def salvar_final_bom(qtd_finais_bons):
    with open("arquivos_salvamento/final_bom", "w") as arquivo:
        arquivo.write(qtd_finais_bons)


def salvar_final_ruim(qtd_finais_ruins):
    with open("arquivos_salvamento/final_ruim", "w") as arquivo:
        arquivo.write(qtd_finais_ruins)


def salvar_jogo_finalizado():
    with open("arquivos_salvamento/jogo_finalizado", "w") as arquivo:
        arquivo.write("1")