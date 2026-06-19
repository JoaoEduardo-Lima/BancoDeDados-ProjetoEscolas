import tkinter as tk

from UI.gerenciador_tema import (
    GerenciadorTema
)

from conexaoDB.conexao import (
    GerenciadorBancoDeDados
)


class Tela_TerminalSQL(tk.Frame):

    def __init__(
        self,
        master,
        app
    ):

        super().__init__(
            master,
            bg=GerenciadorTema.current.WINDOW_BG
        )

        self.app = app

        self.build()

    def build(self):

        titulo = tk.Label(

            self,

            text="Terminal SQL",

            bg=GerenciadorTema.current.WINDOW_BG,

            fg=GerenciadorTema.current.TITLE_FG,

            font=(

                GerenciadorTema.current.FONT_FAMILY,

                24
            )
        )

        titulo.pack(
            pady=20
        )

        self.editor = tk.Text(

            self,

            height=10
        )

        self.editor.pack(

            fill="x",

            padx=20,

            pady=10
        )

        self.btn_executar = tk.Button(

            self,

            text="Executar",

            command=self.executar
        )

        self.btn_executar.pack(
            pady=10
        )

        self.resultado = tk.Text(

            self,

            state="disabled"
        )

        self.resultado.pack(

            fill="both",

            expand=True,

            padx=20,

            pady=10
        )

        self.btn_voltar = tk.Button(

            self,

            text="Voltar",

            command=self.voltar
        )

        self.btn_voltar.pack(
            pady=10
        )

    def executar(self):

        sql = self.editor.get(
            "1.0",
            "end"
        ).strip()

        sucesso, retorno = (
            GerenciadorBancoDeDados
            .execute(sql)
        )

        if sucesso:

            texto = ""

            if isinstance(
                retorno,
                list
            ):

                for linha in retorno:

                    texto += (
                        f"{linha}\n"
                    )

            else:

                texto = str(
                    retorno
                )

        else:

            texto = (
                f"ERRO:\n\n{retorno}"
            )

        self.mostrar_resultado(
            texto
        )

    def mostrar_resultado(
        self,
        texto
    ):

        self.resultado.config(
            state="normal"
        )

        self.resultado.delete(
            "1.0",
            "end"
        )

        self.resultado.insert(
            "1.0",
            texto
        )

        self.resultado.config(
            state="disabled"
        )

    def voltar(self):

        self.app.go_back()