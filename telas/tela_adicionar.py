from core.menu import Menu


class Menu_adicionar(Menu):

    def __init__(self, master, app):

        options = [
            ("Voltar",self.voltar),
            ("Adicionar a Carrinhos", self.terminal),
            ("Adicionar a Máquinas", self.analise),
            ("Adicionar a revisões ", self.adicionar),
            ("Adicionar a ", self.remover)
        ]

        super().__init__(
            master,
            app,
            "MENU ADICIONAR",
            options
        )

    def terminal(self):
        print("Abrir terminal")

    def analise(self):
        print("abrir menu de analise")

    def adicionar(self):
        print("Abrir  menu de adicionar")
    
    def remover(self):
        print("abrir menu de remove")

    def voltar(self):
        self.app.go_back()

   