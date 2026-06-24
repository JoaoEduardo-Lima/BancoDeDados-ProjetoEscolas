from core.menu import Menu
from core.janela import app
from telas.tela_config_bd import *

from telas.tela_selecionar_bd import (Tela_SelecionarSGBD)


class Tela_BancoDados(Menu):

    def __init__(self, master, app):

        options = [
            ("Voltar",self.voltar),
            ("Selecionar SGBD", self.selecionar_sgbd ),
            ("Configurar Conexão",self.configurar),
            ("Testar Conexão",self.testar )
        ]

        super().__init__(
            master,
            app,
            "Banco de Dados",
            options
        )

    def selecionar_sgbd(self):
        
        self.app.show_screen(
            Tela_SelecionarSGBD
        )

    def configurar(self):

        self.app.show_screen(
            Tela_ConfigurarConexao
        )

    def testar(self):

        print(
            "Testar conexão"
        )

    def voltar(self):

        self.app.go_back()