from core.menu import Menu
from telas.menu_principal import Menu_principal
from telas.tela_configuracao import Tela_Configuracao
from conexaoDB.conexao import GerenciadorBancoDeDados


class Tela_inicial(Menu):

    def __init__(self, master, app):

        options = [
            ("Iniciar", self.iniciar),
            ("Configurações", self.configuracao),
            ("Sair", self.sair)
        ]

        if GerenciadorBancoDeDados.is_connected():

            status = "🟢 Conectado"

        else:

            status = "🔴 Desconectado"

        subtitle = (
            f"SGBD: "
            f"{GerenciadorBancoDeDados.current_name}\n"
            f"Status: {status}"
        )

        for campo, valor in (
            GerenciadorBancoDeDados
            .get_config()
            .items()
        ):

            subtitle += (
                f"\n{campo}: {valor}"
            )

        super().__init__(
            master,
            app,
            "Sistema Banco de Dados",
            options,
            subtitle
        )

    def iniciar(self):

        self.app.show_screen(
            Menu_principal
        )

    def configuracao(self):

        self.app.show_screen(
            Tela_Configuracao
        )

    def sair(self):

        self.app.fechar()