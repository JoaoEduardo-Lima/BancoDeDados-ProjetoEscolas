import tkinter as tk


class menu(tk.Frame):

    def __init__(
        self,
        master,
        app,
        title,
        options
    ):

        super().__init__(master, bg="black")

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
            fg="lime",
            bg="black",
            font=("Consolas", 20)
        )

        self.title_label.pack(pady=20)

        self.option_labels = []

        for _ in self.options:

            label = tk.Label(
                self,
                text="",
                fg="white",
                bg="black",
                anchor="w",
                font=("Consolas", 16)
            )

            label.pack(fill="x", padx=40)

            self.option_labels.append(label)

        self.refresh()

    def refresh(self):

        for i, label in enumerate(self.option_labels):

            prefix = ">" if i == self.selected else " "

            label.config(
                text=f"{prefix} {self.options[i][0]}"
            )

    def up(self, event):
        self.selected = (self.selected - 1) % len(self.options)
        self.refresh()

    def down(self, event):
        self.selected = (self.selected + 1) % len(self.options)
        self.refresh()

    def enter(self, event):

        callback = self.options[self.selected][1]

        callback()
