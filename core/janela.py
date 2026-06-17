import tkinter as tk


class Janela:

    def __init__(self):

        self.root = tk.Tk()

        self.root.title("Sistema")

        self.root.geometry("800x600")

        self.root.configure(bg="black")

        self.current_screen = None

        # Histórico
        self.history = []

        # Informações da tela atual
        self.current_class = None
        self.current_kwargs = {}

        self.center_window()


    def show_screen(
        self,
        screen_class,
        add_to_history=True,
        **kwargs
    ):

        if self.current_screen:

            if add_to_history:

                self.history.append(
                    (
                        self.current_class,
                        self.current_kwargs
                    )
                )

            self.current_screen.destroy()

        self.current_class = screen_class
        self.current_kwargs = kwargs

        self.current_screen = screen_class(
            self.root,
            self,
            **kwargs
        )

        self.current_screen.pack(
            fill="both",
            expand=True
        )


    def go_back(self):

        if not self.history:
            return

        screen_class, kwargs = (
            self.history.pop()
        )

        if self.current_screen:
            self.current_screen.destroy()

        self.current_class = screen_class
        self.current_kwargs = kwargs

        self.current_screen = screen_class(
            self.root,
            self,
            **kwargs
        )

        self.current_screen.pack(
            fill="both",
            expand=True
        )


    def refresh_screen(self):

        if not self.current_class:
            return

        self.show_screen(
            self.current_class,
            add_to_history=False,
            **self.current_kwargs
        )


    def clear_history(self):

        self.history.clear()


    def center_window(self):

        self.root.update_idletasks()

        largura = self.root.winfo_width()
        altura = self.root.winfo_height()

        largura_tela = (
            self.root.winfo_screenwidth()
        )

        altura_tela = (
            self.root.winfo_screenheight()
        )

        x = (
            largura_tela // 2
        ) - (
            largura // 2
        )

        y = (
            altura_tela // 2
        ) - (
            altura // 2
        )

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


    def run(self):

        self.root.mainloop()


app = Janela()