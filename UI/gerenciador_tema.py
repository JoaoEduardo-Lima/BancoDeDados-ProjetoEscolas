from UI.tema import (
    DarkTheme,
    LightTheme,
    PastelTheme
)


TEMAS = {

    "DarkTheme":
        DarkTheme,

    "LightTheme":
        LightTheme,

    "PastelTheme":
        PastelTheme
}


class GerenciadorTema:

    current = DarkTheme

    @classmethod
    def set_theme(
        cls,
        tema
    ):

        cls.current = tema

    @classmethod
    def set_theme_by_name(
        cls,
        nome
    ):

        if nome in TEMAS:

            cls.current = (
                TEMAS[nome]
            )

    @classmethod
    def get_theme_name(
        cls
    ):

        return (
            cls.current.__name__
        )