import tkinter as tk

opcoes_inicial = ["Iniciar", "Configurações"]
indice_inicial = 0


def criar_tela_inicial(janela):
    frame_inicial = tk.Frame(janela, bg="black")

    area = tk.Text(
        frame_inicial,
        bg="black",
        fg="white",
        font=("Consolas", 16),
        bd=0,
        highlightthickness=0
    )
    area.pack(fill="both", expand=True)

    return frame_inicial, area

def desenhar_inicial(area):
    global indice_inicial

    area.config(state="normal")
    area.delete("1.0", tk.END)

    largura = 40

    topo = "+" + "-" * largura + "+\n"
    area.insert(tk.END, topo)
    area.insert(tk.END, f"|{'BEM-VINDO':^{largura}}|\n")
    area.insert(tk.END, "|" + " " * largura + "|\n")

    for i, op in enumerate(opcoes_inicial):
        linha = f"> {op}" if i == indice_inicial else f"  {op}"
        area.insert(tk.END, f"| {linha:<{largura-1}}|\n")

    area.insert(tk.END, "|" + " " * largura + "|\n")
    area.insert(tk.END, topo)

    area.config(state="disabled")