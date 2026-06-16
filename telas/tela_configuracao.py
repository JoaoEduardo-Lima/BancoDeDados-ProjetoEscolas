from core.menu import Menu
from core.janela import app
from telas.tela_resolucao import Tela_Resolucao
from telas.tela_cores import Tela_Cores
from telas.tela_bancodedados import Tela_BancoDados

class Tela_Configuracao(Menu):

    def __init__(self, master, app):

        options = [
            ("Voltar",self.voltar),
            ("Resolução", self.resolucao),
            ("Cores", self.cores),
            ("Banco de Dados", self.bancodedados)
        ]

        super().__init__(
            master, 
            app, 
            "Configurações",
            options
        )
    
    def resolucao(self):
        app.show_screen(Tela_Resolucao)

    def cores(self):
        app.show_screen(Tela_Cores)
    
    def bancodedados(self):
        app.show_screen(Tela_BancoDados)

    def voltar(self):
        self.app.go_back()
    
