from core.menu import Menu


class Tela_Resolucao(Menu):

    def __init__(self, master, app):

        options = [
            ("Voltar",self.voltar),
            ("800x600", self.res_800x600),
            ("1024x768", self.res_1024x768),
            ("1280x720", self.res_1280x720),
            ("1366x768", self.res_1366x768),
            ("1920x1080", self.res_1920x1080)
        ]

        super().__init__(
            master,
            app,
            "Resolução",
            options
        )

    def alterar_resolucao(
            self, 
            largura, 
            altura
        ):

        self.app.set_resolution(
            largura,
            altura
        )

    def res_800x600(self):
        self.alterar_resolucao(800, 600)

    def res_1024x768(self):
        self.alterar_resolucao(1024, 768)

    def res_1280x720(self):
        self.alterar_resolucao(1280, 720)

    def res_1366x768(self):
        self.alterar_resolucao(1366, 768)

    def res_1920x1080(self):
        self.alterar_resolucao(1920, 1080)

    def voltar(self):
        self.app.go_back()