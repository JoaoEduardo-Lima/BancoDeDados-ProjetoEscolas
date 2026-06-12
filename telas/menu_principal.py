from core.menu import menu


class Menu_principal(menu):

    def __init__(self, master, app):

        options = [
            ("Clientes", self.clientes),
            ("Produtos", self.produtos),
            ("Sair", app.root.quit)
        ]

        super().__init__(
            master,
            app,
            "MENU PRINCIPAL",
            options
        )

    def clientes(self):
        print("Abrir clientes")

    def produtos(self):
        print("Abrir produtos")