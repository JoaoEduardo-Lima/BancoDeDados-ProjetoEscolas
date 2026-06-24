from tkinter import ttk

from UI.gerenciador_tema import (
GerenciadorTema
)

class ResultView(ttk.Frame):


    def __init__(
        self,
        master
    ):

        super().__init__(master)

        self.tree = None

        self.configurar_estilo()

    def configurar_estilo(self):

        style = ttk.Style()

        style.configure(

            "Terminal.Treeview",

            background=
                GerenciadorTema.current.TREE_BG,

            foreground=
                GerenciadorTema.current.TREE_FG,

            fieldbackground=
                GerenciadorTema.current.TREE_BG,

            rowheight=25
        )

        style.configure(

            "Terminal.Treeview.Heading",

            background=
                GerenciadorTema.current.TREE_HEADER_BG,

            foreground=
                GerenciadorTema.current.TREE_HEADER_FG
        )

    def show_table(
        self,
        colunas,
        linhas
    ):

        if self.tree:

            self.tree.destroy()

        self.tree = ttk.Treeview(

            self,

            style="Terminal.Treeview",

            columns=colunas,

            show="headings"
        )

        for coluna in colunas:

            self.tree.heading(
                coluna,
                text=coluna
            )

            self.tree.column(
                coluna,
                width=120
            )

        for linha in linhas:

            self.tree.insert(
                "",
                "end",
                values=linha
            )

        self.tree.pack(
            fill="both",
            expand=True
        )

