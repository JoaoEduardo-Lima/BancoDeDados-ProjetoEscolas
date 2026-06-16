from core.menu import Menu


class Menu_remover(Menu):

    def __init__(self, master, app):

        options = [
            ("Voltar",self.voltar),
            ("Remover a Carrinhos", self.terminal),
            ("Remover a Máquinas", self.analise),
            ("Remover a revisões ", self.adicionar),
            ("Remover a ", self.remover)
        ]

        super().__init__(
            master,
            app,
            "MENU REMOVER",
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