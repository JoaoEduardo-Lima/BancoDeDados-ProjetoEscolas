import tkinter as tk


# Classe principal responsável pela janela do sistema
class Janela:

    def __init__(self):

        # Cria a janela principal do Tkinter
        self.root = tk.Tk()

        # Define o título exibido na barra da janela
        self.root.title("Sistema")

        # Define a resolução inicial da janela
        self.root.geometry("800x600")

        # Define a cor de fundo da janela
        self.root.configure(bg="black")

        # Guarda a tela atualmente exibida
        self.current_screen = None

        # Pilha de histórico para permitir voltar para telas anteriores
        self.history = []

        # Centraliza a janela na tela do usuário
        self.center_window()


    # Troca a tela atualmente exibida
    def show_screen(self, screen_class):

        # Se já existe uma tela aberta
        if self.current_screen:

            # Salva a classe da tela atual no histórico
            # para permitir retornar depois
            self.history.append(
                self.current_screen.__class__
            )

            # Remove a tela atual da interface
            self.current_screen.destroy()

        # Cria uma nova instância da tela recebida
        self.current_screen = screen_class(
            self.root,
            self
        )

        # Faz a nova tela ocupar toda a janela
        self.current_screen.pack(
            fill="both",
            expand=True
        )


    # Retorna para a tela anterior
    def go_back(self):

        # Se não houver histórico, não faz nada
        if not self.history:
            return

        # Remove e recupera a última tela visitada
        previous_screen = self.history.pop()

        # Remove a tela atual
        if self.current_screen:
            self.current_screen.destroy()

        # Recria a tela anterior
        self.current_screen = previous_screen(
            self.root,
            self
        )

        # Exibe a tela
        self.current_screen.pack(
            fill="both",
            expand=True
        )


    # Centraliza a janela na tela do usuário
    def center_window(self):

        # Atualiza informações internas do Tkinter
        self.root.update_idletasks()

        # Obtém largura atual da janela
        largura = self.root.winfo_width()

        # Obtém altura atual da janela
        altura = self.root.winfo_height()

        # Obtém largura do monitor
        largura_tela = self.root.winfo_screenwidth()

        # Obtém altura do monitor
        altura_tela = self.root.winfo_screenheight()

        # Calcula posição X para centralizar
        x = (largura_tela // 2) - (largura // 2)

        # Calcula posição Y para centralizar
        y = (altura_tela // 2) - (altura // 2)

        # Move a janela para a posição calculada
        self.root.geometry(
            f"{largura}x{altura}+{x}+{y}"
        )


    # Altera a resolução da janela
    def set_resolution(
        self,
        largura,
        altura
    ):

        # Define novo tamanho
        self.root.geometry(
            f"{largura}x{altura}"
        )

        # Recentraliza a janela após redimensionar
        self.center_window()


    # Recria a tela atual
    # Útil para aplicar temas sem alterar o histórico
    def refresh_screen(self):

        # Guarda a classe da tela atual
        current_class = self.current_screen.__class__

        # Remove a tela atual
        self.current_screen.destroy()

        # Cria novamente a mesma tela
        self.current_screen = current_class(
            self.root,
            self
        )

        # Exibe a nova instância da tela
        self.current_screen.pack(
            fill="both",
            expand=True
        )


    # Inicia o loop principal do Tkinter
    # Mantém a aplicação executando
    def run(self):
        self.root.mainloop()


# Instância única da janela utilizada pelo sistema inteiro
app = Janela()