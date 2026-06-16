from core.menu import Menu


class Menu_analise(Menu):

    def __init__(self, master, app):

        options = [
            ("Voltar",self.voltar),
            ("Analisar a Carrinhos", self.terminal),
            ("Analisar a Máquinas", self.analise),
            ("Analisar a revisões ", self.adicionar),
            ("Analisar a ", self.remover)
        ]

        super().__init__(
            master,
            app,
            "MENU ANALISE",
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