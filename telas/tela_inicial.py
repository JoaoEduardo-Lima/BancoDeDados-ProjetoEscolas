from core.menu import Menu
from telas.menu_principal import Menu_principal
from core.janela import app

class Tela_inicial(Menu):

    def __init__(self, master, app):

        options = [
            ("Iniciar", self.iniciar),
            ("Configurações", self.configuracao),
            ("Sair", app.root.quit)
        ]

        super().__init__(
            master, 
            app, 
            "Sistema Banco de Dados",
            options
        )
    
    def iniciar(self):
        app.show_screen(Menu_principal)

    def configuracao(self):
        print("abrir configurações")
