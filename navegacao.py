# Funções para movimentação pelo menu ===========================================================

def lidar_teclado(event, estado, desenhar, animar=None):
    if event.keysym == "Up":
        estado["indice"] = (estado["indice"] - 1) % len(estado["opcoes"])

    elif event.keysym == "Down":
        estado["indice"] = (estado["indice"] + 1) % len(estado["opcoes"])
    else:
        return  # evita redesenho desnecessário

    desenhar()

    if animar:
        animar()

def selecionar(event, estado):
    opcao = estado["opcoes"][estado["indice"]]
    acao = estado["acoes"].get(opcao)

    if acao:
        acao()

def animar_selecao(janela, menu_area):
    menu_area.tag_config("selecionado", background="#00AA00")
    janela.after(80, lambda: menu_area.tag_config("selecionado", background="#003300"))