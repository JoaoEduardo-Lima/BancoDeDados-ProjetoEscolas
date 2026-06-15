import tkinter as tk


class Janela:

    def __init__(self):

        self.root = tk.Tk()

        self.root.title("Sistema")

        self.root.geometry("800x600")

        self.root.configure(bg="black")

        self.current_screen = None

        self.history = []

        self.center_window()

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

    def center_window(self):

        self.root.update_idletasks()

        largura = self.root.winfo_width()
        altura = self.root.winfo_height()

        largura_tela = self.root.winfo_screenwidth()
        altura_tela = self.root.winfo_screenheight()

        x = (largura_tela // 2) - (largura // 2)
        y = (altura_tela // 2) - (altura // 2)

        self.root.geometry(
            f"{largura}x{altura}+{x}+{y}"
        )

    def set_resolution(
        self,
        largura,
        altura
        ):

        self.root.geometry(
            f"{largura}x{altura}"
        )

        self.center_window()

    def refresh_screen(self):

        current_class = self.current_screen.__class__

        self.current_screen.destroy()

        self.current_screen = current_class(
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