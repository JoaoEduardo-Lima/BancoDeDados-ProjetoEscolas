import tkinter as tk

from UI.estilo import MenuItemStyle
from UI.gerenciador_tema import GerenciadorTema
from UI.animacao import MenuAnimations


class Menu(tk.Frame):

    def __init__(
        self,
        master,
        app,
        title,
        options
    ):

        super().__init__(
            master,
            bg=GerenciadorTema.current.WINDOW_BG       
        )

        self.app = app
        self.title = title
        self.options = options
        self.selected = 0

        self.build()

        self.bind_all("<Up>", self.up)
        self.bind_all("<Down>", self.down)
        self.bind_all("<Return>", self.enter)

    def build(self):

        self.title_label = tk.Label(
            self,
            text=self.title,
            fg=GerenciadorTema.current.TITLE_FG,
            bg=GerenciadorTema.current.WINDOW_BG,
            font=(
                GerenciadorTema.current.FONT_FAMILY,
                GerenciadorTema.current.TITLE_SIZE
            )
        )

        self.title_label.pack(pady=20)

        self.option_labels = []

        for _ in self.options:

            label = tk.Label(
                self,
                text="",
                anchor="w",
                font=(
                    GerenciadorTema.current.FONT_FAMILY,
                    GerenciadorTema.current.OPTION_SIZE
                )
            )

            label.pack(
                fill="x",
                padx=40
            )

            self.option_labels.append(label)

        self.refresh()

    def apply_style(
        self,
        label,
        style
    ):

        label.config(**style)

    def render_option(self, index):

        label = self.option_labels[index]

        if index == self.selected:

            self.apply_style(
                label,
                MenuItemStyle.selected()
            )

            label.config(
                text=f"> {self.options[index][0]}"
            )

        else:

            self.apply_style(
                label,
                MenuItemStyle.normal()
            )

            label.config(
                text=f"  {self.options[index][0]}"
            )

    def refresh(self):

        for i in range(len(self.options)):
            self.render_option(i)

    def up(self, event):

        self.selected = (
            self.selected - 1
        ) % len(self.options)

        self.refresh()

    def down(self, event):

        self.selected = (
            self.selected + 1
        ) % len(self.options)

        self.refresh()

    def enter(self, event):

        MenuAnimations.on_select(
            self.option_labels[self.selected]
        )

        callback = self.options[self.selected][1]

        callback()

