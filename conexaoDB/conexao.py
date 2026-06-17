class GerenciadorBancoDeDados:

    current_driver = None

    current_name = "Nenhum"

    conexao = None

    # Guarda todos os parâmetros da conexão
    connection_data = {}

    @classmethod
    def set_driver(
        cls,
        driver,
        name
    ):

        cls.current_driver = driver
        cls.current_name = name

        # limpa configurações do banco anterior
        cls.connection_data = {}

    @classmethod
    def set_value(
        cls,
        campo,
        valor
    ):

        cls.connection_data[campo] = valor

    @classmethod
    def get_value(
        cls,
        campo
    ):

        return cls.connection_data.get(
            campo,
            ""
        )

    @classmethod
    def get_all_values(cls):

        return cls.connection_data

    @classmethod
    def connect(cls):

        if not cls.current_driver:

            print(
                "Nenhum banco selecionado."
            )

            return False

        try:

            cls.conexao = (
                cls.current_driver.connect(
                    cls.connection_data
                )
            )

            print(
                "Conectado!"
            )

            return True

        except Exception as erro:

            print(
                f"Erro: {erro}"
            )

            return False

    @classmethod
    def disconnect(cls):

        if cls.conexao:

            cls.conexao.close()

            cls.conexao = None

            print(
                "Desconectado."
            )