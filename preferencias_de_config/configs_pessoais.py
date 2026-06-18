import json
import os


class Configuracoes:

    ARQUIVO = "preferencias_de_config/personal_settings.json"

    @classmethod
    def carregar(cls):

        if not os.path.exists(cls.ARQUIVO):

            return {}

        with open(
            cls.ARQUIVO,
            "r",
            encoding="utf-8"
        ) as arquivo:

            return json.load(arquivo)

    @classmethod
    def salvar(
        cls,
        dados
    ):

        with open(
            cls.ARQUIVO,
            "w",
            encoding="utf-8"
        ) as arquivo:

            json.dump(
                dados,
                arquivo,
                indent=4
            )


