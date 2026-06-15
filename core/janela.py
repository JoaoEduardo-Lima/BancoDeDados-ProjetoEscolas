import tkinter as tk


class Janela:

    def __init__(self):

        self.root = tk.Tk()

        self.root.title("Sistema")
        self.root.geometry("800x600")

        self.root.configure(bg="black")

        self.current_screen = None

        # Histórico de telas
        self.history = []

    def show_screen(self, screen_class):

        # Salva a tela atual antes de trocar
        if self.current_screen:

            self.history.append(
                self.current_screen.__class__
            )

            self.current_screen.destroy()

        self.current_screen = screen_class(
            self.root,
            self
        )

        self.current_screen.pack(
            fill="both",
            expand=True
        )

    def go_back(self):

        if not self.history:
            return

        previous_screen = self.history.pop()

        if self.current_screen:
            self.current_screen.destroy()

        self.current_screen = previous_screen(
            self.root,
            self
        )

        self.current_screen.pack(
            fill="both",
            expand=True
        )

    def run(self):
        self.root.mainloop()


app = Janela()