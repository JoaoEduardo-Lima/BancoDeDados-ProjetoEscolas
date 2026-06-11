import tkinter as tk

# Definição da base da janela do terminal q será utilizada no terminal =========================

def criar_janela():
    janela = tk.Tk() # definir a janela base para o terminal
    janela.title("TerminalBD Máquinas Padilha") # Título da janela
    janela.geometry("1200x1000") # Dimensão base (pode ser alterada)
    janela.configure(bg="black") # Cor do background (pode ser alterada)
    return janela # retorno da janela

janela = criar_janela() # definição dos valores acima na var janela

# ===============================================================================================