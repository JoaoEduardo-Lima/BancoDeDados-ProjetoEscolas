import tkinter as tk
from ui.janela import *
from navegacao import *
# Criação da base do Menu de Opções ===============================================================

frame_menu = tk.Frame(janela, bg="black") # Criação do container que apresenta o menu, dentro da janela
frame_menu.pack(fill="both", expand=True) # Coloca o frame na janela, e o expande x e y disponivel

menu_area = tk.Text( # definição dos caracteres
    frame_menu,
    bg="black",
    fg="#FFFFFF",
    font=("Consolas", 14),
    bd=0,
    highlightthickness=0
)

menu_area.pack(fill="both", expand=True, padx=20, pady=20) # definição do espaço tomado pelos caracteres
menu_area.config(state="disabled") # modo apenas leitura

# ===================================================================================================

#lista de opções do menu ============================================================================

estado_menu = {
    "indice": 0,
    "opcoes": ["Abrir Terminal SQL", "Listar Carrinhos", "Sair"],
    "acoes": {
        "Abrir Terminal SQL": abrir_terminal,
        "Listar Carrinhos": listar_carrinhos,
        "Sair": janela.quit
    }
}

#  ===================================================================================================

# Criação do desenho responsivo do menu ==============================================================

def calcular_largura(menu_area): # Cálculo para determinar a área utilizada
    largura_pixels = menu_area.winfo_width() # Recebe a largura do menu área
    largura_chars = max(30, int(largura_pixels / 10)) # converte o tamnho recebido de pixel para quantidade de caracteres com limite de 30 de tamanho mínimo
    return largura_chars - 4 # garante q n ira atrapalhar as bordas

def desenhar_menu(menu_area, estado):
    largura = calcular_largura(menu_area)

    topo = "+" + "-" * largura + "+\n"
    base = "+" + "-" * largura + "+\n"

    menu_area.config(state="normal")
    menu_area.delete("1.0", tk.END)

    menu_area.insert(tk.END, topo)
    menu_area.insert(tk.END, f"|{'MENU PRINCIPAL':^{largura}}|\n")
    menu_area.insert(tk.END, "|" + " " * largura + "|\n")

    for i, op in enumerate(estado["opcoes"]):
        linha = f"> {op}" if i == estado["indice"] else f"  {op}"
        texto_linha = f"| {linha:<{largura-1}}|\n"

        linha_inicio = menu_area.index("end-1c linestart")
        menu_area.insert(tk.END, texto_linha)

        colunas = len(texto_linha.strip("\n"))
        linha_fim = f"{linha_inicio}+{colunas}c"

        if i == estado["indice"]:
            menu_area.tag_add("selecionado", linha_inicio, linha_fim)

    menu_area.insert(tk.END, "|" + " " * largura + "|\n")
    menu_area.insert(tk.END, base)

    menu_area.tag_config("selecionado", background="#003300", foreground="#00FF00")
    menu_area.config(state="disabled")

# ==============================================================================================


# Animação de Seleção ==========================================================================

    menu_area.tag_config("selecionado", background="#003300", foreground="#00FF00")
    menu_area.config(state="disabled")

def animar_selecao(janela, menu_area):
    menu_area.tag_config("selecionado", background="#00AA00")
    janela.after(80, lambda: menu_area.tag_config("selecionado", background="#003300"))

# ===============================================================================================

# Funções para movimentação pelo menu ===========================================================







def selecionar(event, janela, menu_area, abrir_terminal):
    opcao = opcoes[indice]

    if opcao == "Sair":
        janela.quit()

    elif opcao == "Abrir Terminal SQL":
        abrir_terminal()

    else:
        menu_area.config(text=f"> {opcao}\n\n[Em desenvolvimento]")

# =================================================================================================