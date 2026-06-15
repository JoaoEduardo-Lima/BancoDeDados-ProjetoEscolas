from core.menu import Menu
from core.janela import app
from telas.tela_resolucao import Tela_Resolucao
from telas.tela_cores import Tela_Cores

class Tela_Configuracao(Menu):

    def __init__(self, master, app):

        options = [
            ("Resolução", self.resolucao),
            ("Cores", self.cores),
            ("voltar", self.voltar)
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

    def voltar(self):
        self.app.go_back()