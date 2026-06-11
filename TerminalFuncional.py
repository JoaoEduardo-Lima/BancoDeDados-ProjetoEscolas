import pyodbc
import tkinter as tk
from tkinter import scrolledtext

# ==============================
# CONFIG BANCO
# ==============================

server = 'localhost\\SQLEXPRESS01'
database = 'MaquinasPadilha'

conn_str = f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;'

# ==============================
# CONEXÃO
# ==============================

def conectar():
    try:
        return pyodbc.connect(conn_str)
    except Exception as e:
        print("Erro conexão:", e)
        return None


# ==============================
# JANELA
# ==============================

janela = tk.Tk()
janela.title("TerminalBD Máquinas Padilha")
janela.geometry("800x500")
janela.configure(bg="black")

# ==============================
# FRAMES (TELAS)
# ==============================

frame_menu = tk.Frame(janela, bg="black")
frame_terminal = tk.Frame(janela, bg="black")

frame_menu.pack(fill="both", expand=True)

# ==============================
# MENU
# ==============================

opcoes = [
    "Abrir Terminal SQL",
    "Listar Carrinhos",
    "Sair"
]

indice = 0

menu_area = tk.Text(
    frame_menu,
    bg="black",
    fg="#FFFFFF",
    font=("Consolas", 14),
    bd=0,
    highlightthickness=0
)

menu_area.pack(fill="both", expand=True, padx=20, pady=20)

menu_area.config(state="disabled")  # impede o usuário de editar

def calcular_largura():
    # largura da janela em pixels → converte pra "caracteres"
    largura_pixels = menu_area.winfo_width()

    # cada char ≈ 10px (Consolas 14)
    largura_chars = max(30, int(largura_pixels / 10))

    return largura_chars - 4

janela.update_idletasks()

def desenhar_menu():
    largura = calcular_largura()

    topo = "+" + "-" * largura + "+\n"
    base = "+" + "-" * largura + "+\n"

    menu_area.config(state="normal")
    menu_area.delete("1.0", tk.END)

    menu_area.insert(tk.END, topo)
    menu_area.insert(tk.END, f"|{'MENU PRINCIPAL':^{largura}}|\n")
    menu_area.insert(tk.END, "|" + " " * largura + "|\n")

    for i, op in enumerate(opcoes):
        linha = f"> {op}" if i == indice else f"  {op}"
        texto_linha = f"| {linha:<{largura-1}}|\n"

        # pega número da linha antes de inserir
        linha_inicio = menu_area.index("end-1c linestart")

        menu_area.insert(tk.END, texto_linha)

        # pega o fim da linha mas limita pelo tamanho real do texto
        colunas = len(texto_linha.strip("\n"))
        linha_fim = f"{linha_inicio}+{colunas}c"

        if i == indice:
            menu_area.tag_add("selecionado", linha_inicio, linha_fim)
    menu_area.insert(tk.END, "|" + " " * largura + "|\n")
    menu_area.insert(tk.END, base)

    menu_area.tag_config("selecionado", background="#003300", foreground="#00FF00")
    menu_area.tag_config(
    "selecionado",
    background="#003300",
    foreground="#00FF00"
)
    menu_area.config(state="disabled")
 
def animar_selecao():
    menu_area.tag_config("selecionado", background="#00AA00")
    janela.after(80, lambda: menu_area.tag_config("selecionado", background="#003300"))


def mover_cima(event):
    global indice
    indice = (indice - 1) % len(opcoes)
    desenhar_menu()
    animar_selecao()


def mover_baixo(event):
    global indice
    indice = (indice + 1) % len(opcoes)
    desenhar_menu()
    animar_selecao()


def selecionar(event):
    opcao = opcoes[indice]

    if opcao == "Sair":
        janela.quit()

    elif opcao == "Abrir Terminal SQL":
        abrir_terminal()

    else:
        menu_area.config(text=f"> {opcao}\n\n[Em desenvolvimento]")


# ==============================
# TERMINAL
# ==============================

def abrir_terminal():
    frame_menu.pack_forget()
    frame_terminal.pack(fill="both", expand=True)


def voltar_menu():
    frame_terminal.pack_forget()
    frame_menu.pack(fill="both", expand=True)


output_area = scrolledtext.ScrolledText(
    frame_terminal,
    bg="black",
    fg="#FFFFFF",
    insertbackground="#FFFFFF",
    font=("Consolas", 11),
    
)

output_area.pack(expand=True, fill='both')

frame_input = tk.Frame(frame_terminal, bg="black")
frame_input.pack(fill='x')

prompt = tk.Label(
    frame_input,
    text=">",
    bg="black",
    fg="#FFFFFF",
    font=("Consolas", 11)
)
prompt.pack(side="left")

entrada = tk.Entry(
    frame_input,
    bg="black",
    fg="#FFFFFF",
    insertbackground="#FFFFFF",
    font=("Consolas", 11),
    borderwidth=0
)
entrada.pack(side="left", fill="x", expand=True)


def executar_comando(event=None):
    comando = entrada.get()
    entrada.delete(0, tk.END)

    if comando.lower() == "voltar":
        voltar_menu()
        return

    output_area.insert(tk.END, f"> {comando}\n")

    try:
        cursor.execute(comando)

        if comando.lower().startswith("select"):
            colunas = [c[0] for c in cursor.description]
            output_area.insert(tk.END, " | ".join(colunas) + "\n")

            for row in cursor.fetchall():
                output_area.insert(tk.END, " | ".join(map(str, row)) + "\n")
        else:
            conn.commit()
            output_area.insert(tk.END, "✔ OK\n")

    except Exception as e:
        output_area.insert(tk.END, f"✖ Erro: {e}\n")

    output_area.insert(tk.END, "\n")
    output_area.see(tk.END)


entrada.bind("<Return>", executar_comando)

# ==============================
# BINDS MENU
# ==============================

janela.bind("<Up>", mover_cima)
janela.bind("<Down>", mover_baixo)
janela.bind("<Return>", selecionar)

# ==============================
# BANCO
# ==============================

conn = conectar()
if conn:
    cursor = conn.cursor()

# ==============================
# START
# ==============================

janela.after(50, desenhar_menu)
janela.mainloop()