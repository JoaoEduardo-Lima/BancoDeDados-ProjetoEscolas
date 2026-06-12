import tkinter as tk

from UI.estilo import MenuItemStyle
from UI.tema import Theme
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
            bg=Theme.WINDOW_BG
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
            fg=Theme.TITLE_FG,
            bg=Theme.WINDOW_BG,
            font=(
                Theme.FONT_FAMILY,
                Theme.TITLE_SIZE
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
                    Theme.FONT_FAMILY,
                    Theme.OPTION_SIZE
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
                MenuItemStyle.SELECTED
            )

            label.config(
                text=f"> {self.options[index][0]}"
            )

        else:

            self.apply_style(
                label,
                MenuItemStyle.NORMAL
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

