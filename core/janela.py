import tkinter as tk #fundação do programa, nossass janelas são feitas por ele
from preferencias_de_config.configs_pessoais import Configuracoes # import das configurações salvas da ultima sessão
from UI.gerenciador_tema import GerenciadorTema #import dos possíveis temas de cor do aplicativo
from conexaoDB.conexao import GerenciadorBancoDeDados # import da classe responsavel pelo gerenciamento e conexao com o database
from conexaoDB.drivers_map import DRIVERS # import das configurações especificas de cada drive


class Janela: #classe responsável por ser a base do nosso programa, nosso app

    def __init__(self):
        self.root = tk.Tk()

        dados = Configuracoes.carregar()

        tema = dados.get("tema", "DarkTheme")
        GerenciadorTema.set_theme_by_name(tema)

        sgbd = dados.get("sgbd",None)
        if sgbd in DRIVERS:
            GerenciadorBancoDeDados.set_driver(

                DRIVERS[sgbd](),

                sgbd
        )   
            
        config_db = dados.get("config_db",{})
        GerenciadorBancoDeDados.set_config(config_db)
        
        largura = dados.get("largura",800)
        altura = dados.get("altura",600)
        
        self.root.geometry(f"{largura}x{altura}")
        
        self.root.title("Sistema")

        self.root.configure(bg="black")

        self.current_screen = None

        self.message = ""

        # Histórico
        self.history = []

        # Informações da tela atual 
        self.current_class = None

        self.current_kwargs = {}

        self.center_window()

        self.root.protocol("WM_DELETE_WINDOW",self.fechar)

    def show_screen(
        self,
        screen_class,
        add_to_history=True,
        **kwargs
    ):

        if self.current_screen:

            if add_to_history:

                self.history.append(
                    (
                        self.current_class,
                        self.current_kwargs
                    )
                )

            self.current_screen.destroy()

        self.current_class = screen_class
        self.current_kwargs = kwargs

        self.current_screen = screen_class(
            self.root,
            self,
            **kwargs
        )

        self.current_screen.pack(
            fill="both",
            expand=True
        )


    def go_back(self):

        if not self.history:
            return

        screen_class, kwargs = (
            self.history.pop()
        )

        if self.current_screen:
            self.current_screen.destroy()

        self.current_class = screen_class
        self.current_kwargs = kwargs

        self.current_screen = screen_class(
            self.root,
            self,
            **kwargs
        )

        self.current_screen.pack(
            fill="both",
            expand=True
        )


    def refresh_screen(self):

        if not self.current_class:
            return

        self.show_screen(
            self.current_class,
            add_to_history=False,
            **self.current_kwargs
        )


    def clear_history(self):

        self.history.clear()


    def center_window(self):

        self.root.update_idletasks()

        largura = self.root.winfo_width()
        altura = self.root.winfo_height()

        largura_tela = (
            self.root.winfo_screenwidth()
        )

        altura_tela = (
            self.root.winfo_screenheight()
        )

        x = (
            largura_tela // 2
        ) - (
            largura // 2
        )

        y = (
            altura_tela // 2
        ) - (
            altura // 2
        )

        self.root.geometry(
            f"{largura}x{altura}+{x}+{y}"
        )


    def set_resolution(
        self,
        largura,
        altura
    ):

        self.root.geometry(
            f"{largura}x{altura}"
        )

        self.center_window()

    def set_message(
        self,
        texto
    ):

        self.message = texto

    def get_message(self):

        return self.message


    def salvar_configuracoes(self):

        dados = {

            "largura":
                self.root.winfo_width(),

            "altura":
                self.root.winfo_height(),

            "tema":
                GerenciadorTema
                .get_theme_name(),

            "sgbd":
                GerenciadorBancoDeDados
                .current_name,

            "config_db":
                GerenciadorBancoDeDados
                .get_config()
        }

        Configuracoes.salvar(
            dados
        )

    def fechar(self):

        self.salvar_configuracoes()

        self.root.destroy()

    def run(self):

        self.root.mainloop()


app = Janela()
