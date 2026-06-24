import tkinter as tk

from core.terminal_db.terminal import SQLTerminal


class Tela_TerminalSQL(tk.Frame):

    def __init__(self, master, app):

        super().__init__(master)

        SQLTerminal(
            self,
            app
        ).pack(
            fill="both",
            expand=True
        )
