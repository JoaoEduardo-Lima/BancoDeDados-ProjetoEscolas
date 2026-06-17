from core.menu import Menu

from core.input import InputScreen

from conexaoDB.conexao import (
    GerenciadorBancoDeDados
)


class Tela_ConfigurarConexao(Menu):

    def __init__(
        self,
        master,
        app
    ):

        campos = (
            GerenciadorBancoDeDados
            .current_driver
            .get_connection_fields()
        )

        subtitle = ""

        mensagem = app.get_message()

        if mensagem:

            subtitle += (
                f"{mensagem}\n\n"
            )

        for campo in campos:

            valor = (
                GerenciadorBancoDeDados
                .get_value(campo)
            )

            subtitle += (
                f"{campo}: {valor}\n"
            )

        options = []

        for campo in campos:

            options.append(
                (
                    campo,
                    lambda c=campo:
                    self.editar_campo(c)
                )
            )

        options.append(
            (
                "Testar Conexão",
                self.testar_conexao
            )
        )

        options.append(
            (
                "Conectar",
                self.conectar
            )
        )

        options.append(
            (
                "Voltar",
                self.voltar
            )
        )

        super().__init__(
            master,
            app,
            "Configuração de Conexão",
            options,
            subtitle
        )

    def editar_campo(
        self,
        campo
    ):

        self.app.show_screen(

            InputScreen,

            titulo=f"Digite {campo}",

            valor_inicial=
                GerenciadorBancoDeDados
                .get_value(campo),

            callback=
                lambda valor:
                self.salvar_campo(
                    campo,
                    valor
                )
        )

    def salvar_campo(
        self,
        campo,
        valor
    ):

        GerenciadorBancoDeDados.set_value(
            campo,
            valor
        )

        self.app.go_back()

        self.app.refresh_screen()

    def testar_conexao(self):

        sucesso = (
            GerenciadorBancoDeDados
            .connect()
        )

        if sucesso:

            print(
                "Conexão OK"
            )

        else:

            print(
                "Falha na conexão"
            )


    def voltar(self):

        self.app.go_back()

    def conectar(self):

        sucesso, mensagem = (
            GerenciadorBancoDeDados.connect()
        )

        self.app.set_message(
            mensagem
        )

        self.app.refresh_screen()