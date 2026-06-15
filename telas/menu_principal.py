from core.menu import Menu


class Menu_principal(Menu):

    def __init__(self, master, app):

        options = [
            ("Terminal", self.terminal),
            ("Checar dados das tabelas", self.analise),
            ("Adicionar a tabelas", self.adicionar),
            ("Remover de tabelas", self.remover),
            ("Voltar", self.voltar)
        ]

        super().__init__(
            master,
            app,
            "MENU PRINCIPAL",
            options
        )

    def terminal(self):
        print("Abrir terminal")

    def analise(self):
        print("abrir meni de analise")

    def adicionar(self):
        print("Abrir  menu de adicionar")
    
    def remover(self):
        print("abrir menu de remove")

    def voltar(self):
        self.app.go_back()