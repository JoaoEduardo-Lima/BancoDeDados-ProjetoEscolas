import tkinter as tk


class Janela:

    def __init__(self):

        self.root = tk.Tk()

        self.root.title("Sistema")
        self.root.geometry("800x600")

        self.root.configure(bg="black")

        self.current_screen = None

    def show_screen(self, screen_class):

        if self.current_screen:
            self.current_screen.destroy()

        self.current_screen = screen_class(self.root, self)

        self.current_screen.pack(
            fill="both",
            expand=True
        )

    def run(self):
        self.root.mainloop()

app = Janela()