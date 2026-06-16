from core.menu import Menu
from telas.tela_adicionar import *
from telas.tela_analise import *
from telas.tela_remover import *
from core.janela import app

class Menu_principal(Menu):

    def __init__(self, master, app):

        options = [
            ("Voltar",self.voltar),
            ("Terminal", self.terminal),
            ("Checar dados das tabelas", self.analise),
            ("Adicionar a tabelas", self.adicionar),
            ("Remover de tabelas", self.remover)
        ]

        super().__init__(
            master,
            app,
            "MENU PRINCIPAL",
            options
        )

    def terminal(self):
        print("terminal")

    def analise(self):
        app.show_screen(Menu_analise)

    def adicionar(self):
        app.show_screen(Menu_adicionar)
    
    def remover(self):
        app.show_screen(Menu_remover)

    def voltar(self):
        self.app.go_back()