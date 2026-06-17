import tkinter as tk

from UI.gerenciador_tema import (
    GerenciadorTema
)


class InputScreen(tk.Frame):

    def __init__(
        self,
        master,
        app,
        titulo,
        callback,
        valor_inicial=""
    ):

        super().__init__(
            master,
            bg=GerenciadorTema.current.WINDOW_BG
        )

        self.app = app

        self.titulo = titulo

        self.callback = callback

        self.valor_inicial = valor_inicial

        self.build()


    def build(self):

        self.title_label = tk.Label(

            self,

            text=self.titulo,

            fg=GerenciadorTema.current.TITLE_FG,

            bg=GerenciadorTema.current.WINDOW_BG,

            font=(
                GerenciadorTema.current.FONT_FAMILY,
                20
            )
        )

        self.title_label.pack(
            pady=20
        )


        self.entry = tk.Entry(

            self,

            font=(
                GerenciadorTema.current.FONT_FAMILY,
                14
            ),

            width=40
        )

        self.entry.pack(
            pady=20
        )


        self.entry.insert(
            0,
            self.valor_inicial
        )


        self.entry.focus_set()


        self.bind_all(
            "<Return>",
            self.confirmar
        )

        self.bind_all(
            "<Escape>",
            self.cancelar
        )


    def confirmar(
        self,
        event=None
    ):

        valor = self.entry.get()

        self.callback(
            valor
        )


    def cancelar(
        self,
        event=None
    ):

        self.app.go_back()