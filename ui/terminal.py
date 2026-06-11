import tkinter as tk
from tkinter import scrolledtext
from ui.menu import *
from db.conexao import *

# Criação do frame do terminal ========================================================================

frame_terminal = tk.Frame(janela, bg="black")

def criar_terminal(frame_terminal):

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

    return output_area, entrada

output_area, entrada = criar_terminal(frame_terminal)

# ===============================================================================================

# Funcão para fechar menu e abrir terminal # ====================================================
def abrir_terminal():
    frame_menu.pack_forget()
    frame_terminal.pack(fill="both", expand=True)

# ===============================================================================================

# Função para fechar o terminal e voltar para o menu  ===========================================

def voltar_menu():
    frame_terminal.pack_forget()
    frame_menu.pack(fill="both", expand=True)

# ===============================================================================================

# Funcionalidade do terminal com o Server sql  ==================================================
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

janela.bind("<Up>", lambda e: mover_cima(e, janela, menu_area))
janela.bind("<Down>", lambda e: mover_baixo(e, janela, menu_area))
janela.bind("<Return>", lambda e: selecionar(e, janela, menu_area, abrir_terminal))

# ===============================================================================================