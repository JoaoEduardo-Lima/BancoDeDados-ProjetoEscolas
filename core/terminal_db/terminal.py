import tkinter as tk

from UI.gerenciador_tema import (
GerenciadorTema
)

from conexaoDB.conexao import (
GerenciadorBancoDeDados
)

from core.terminal_db.result_view import (
ResultView
)

from core.terminal_db.query_executor import (
QueryExecutor
)

from core.terminal_db.schema_loader import (
SchemaLoader
)

class SQLTerminal(tk.Frame):

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

        self.bind_all(
            "<F5>",
            lambda e: self.executar()
        )

    def build(self):

        self.criar_header()

        self.criar_layout_principal()

        self.carregar_tabelas()

    def criar_header(self):

        status = (
            "🟢 Conectado"
            if GerenciadorBancoDeDados.is_connected()
            else "🔴 Desconectado"
        )

        banco = (
            GerenciadorBancoDeDados
            .get_value("Banco")
        )

        titulo = tk.Label(

            self,

            text=(
                f"{GerenciadorBancoDeDados.current_name}"
                f" | "
                f"{banco}"
                f" | "
                f"{status}"
            ),

            bg=GerenciadorTema.current.WINDOW_BG,

            fg=GerenciadorTema.current.TITLE_FG,

            font=(
                GerenciadorTema.current.FONT_FAMILY,
                12
            )
        )

        titulo.pack(
            fill="x",
            pady=10
        )

    def criar_layout_principal(self):

        self.main_frame = tk.Frame(
            self
        )

        self.main_frame.pack(
            fill="both",
            expand=True
        )

        self.sidebar = tk.Frame(
            self.main_frame,
            width=200
        )

        self.sidebar.pack(
            side="left",
            fill="y"
        )

        self.area_direita = tk.Frame(
            self.main_frame
        )

        self.area_direita.pack(
            side="left",
            fill="both",
            expand=True
        )

        self.lista_tabelas = tk.Listbox(
            self.sidebar
        )

        self.lista_tabelas.pack(
            fill="both",
            expand=True,
            padx=5,
            pady=5
        )

        self.lista_tabelas.bind(
            "<Double-Button-1>",
            self.inserir_select
        )

        self.editor = tk.Text(
            self.area_direita,
            height=8
        )

        self.editor.pack(
            fill="x",
            padx=10,
            pady=10
        )

        self.editor.insert(
            "1.0",
            "-- Digite seu SQL aqui"
        )

        frame_botoes = tk.Frame(
            self.area_direita
        )

        frame_botoes.pack(
            fill="x"
        )

        tk.Button(
            frame_botoes,
            text="Executar (F5)",
            command=self.executar
        ).pack(
            side="left",
            padx=5
        )

        tk.Button(
            frame_botoes,
            text="Voltar",
            command=self.voltar
        ).pack(
            side="left",
            padx=5
        )

        self.resultado = ResultView(
            self.area_direita
        )

        self.resultado.pack(
            fill="both",
            expand=True,
            padx=10,
            pady=10
        )

    def carregar_tabelas(self):

        tabelas = (
            SchemaLoader
            .carregar_tabelas()
        )

        self.lista_tabelas.delete(
            0,
            tk.END
        )

        for tabela in tabelas:

            self.lista_tabelas.insert(
                tk.END,
                tabela
            )

    def inserir_select(
        self,
        event
    ):

        selecionado = (
            self.lista_tabelas
            .curselection()
        )

        if not selecionado:

            return

        tabela = (
            self.lista_tabelas
            .get(
                selecionado[0]
            )
        )

        self.editor.delete(
            "1.0",
            "end"
        )

        self.editor.insert(
            "1.0",
            f"SELECT * FROM {tabela};"
        )

    def executar(self):

        sql = self.editor.get(
            "1.0",
            "end"
        ).strip()

        if not sql:

            return

        sucesso, resultado = (
            QueryExecutor
            .executar(sql)
        )

        if not sucesso:

            self.resultado.show_message(
                resultado
            )

            return

        if resultado["tipo"] == "SELECT":

            self.resultado.show_table(
                resultado["colunas"],
                resultado["linhas"]
            )

            return

        self.resultado.show_message(
            f"Linhas afetadas: "
            f"{resultado['linhas_afetadas']}"
        )

    def voltar(self):

        self.app.go_back()

