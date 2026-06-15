from UI.gerenciador_tema import GerenciadorTema


class MenuItemStyle:

    @staticmethod
    def normal():

        return {
            "bg": GerenciadorTema.current.NORMAL_BG,
            "fg": GerenciadorTema.current.NORMAL_FG
        }

    @staticmethod
    def selected():

        return {
            "bg": GerenciadorTema.current.SELECTED_BG,
            "fg": GerenciadorTema.current.SELECTED_FG
        }