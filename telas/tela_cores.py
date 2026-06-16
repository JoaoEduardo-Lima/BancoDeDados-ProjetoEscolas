from core.menu import Menu
from UI.gerenciador_tema import GerenciadorTema
from UI.tema import *



class Tela_Cores(Menu):

    def __init__(self, master, app):

        options = [
            ("Voltar",self.voltar),
            ("Modo Escuro", self.dark),
            ("Modo Claro", self.light),
            ("Modo Pastel", self.pastel)
        ]

        super().__init__(
            master,
            app,
            "Cores",
            options
        )

    def dark(self):

        GerenciadorTema.current = DarkTheme

        self.recarregar()

    def light(self):

        GerenciadorTema.current = LightTheme

        self.recarregar()

    def pastel(self):

        GerenciadorTema.current = PastelTheme

        self.recarregar()        

    def recarregar(self):

        self.app.refresh_screen()

    def voltar(self):
        self.app.go_back()