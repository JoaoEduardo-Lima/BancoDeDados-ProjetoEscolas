from core.menu import Menu
from core.janela import app

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
        print("abrir menu de resoluções")

    def cores(self):
        print("abrir menu de cores")

    def voltar(self):
        self.app.go_back()