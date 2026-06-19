class GerenciadorBancoDeDados:

    current_driver = None

    current_name = "Nenhum"

    conexao = None

    config = {}

    @classmethod
    def set_driver(
        cls,
        driver,
        name
    ):

        cls.current_driver = driver
        cls.current_name = name

    @classmethod
    def get_driver(cls):

        return cls.current_driver

    @classmethod
    def get_driver_name(cls):

        return cls.current_name

    @classmethod
    def set_value(
        cls,
        campo,
        valor
    ):

        cls.config[campo] = valor

    @classmethod
    def get_value(
        cls,
        campo
    ):

        return cls.config.get(
            campo,
            ""
        )

    @classmethod
    def get_config(cls):

        return cls.config

    @classmethod
    def set_config(
        cls,
        dados
    ):

        cls.config = dados

    @classmethod
    def connect(cls):

        if not cls.current_driver:

            return (
                False,
                "Nenhum banco selecionado."
            )

        try:

            cls.conexao = (
                cls.current_driver.connect(
                    cls.config
                )
            )

            return (
                True,
                "Conexão realizada com sucesso."
            )

        except Exception as erro:

            return (
                False,
                str(erro)
            )

    @classmethod
    def disconnect(cls):

        if cls.conexao:

            cls.conexao.close()

            cls.conexao = None

    @classmethod
    def is_connected(cls):

        return cls.conexao is not None

    @classmethod
    def get_connection(cls):

        return cls.conexao

    @classmethod
    def execute(
        cls,
        sql
    ):

        if not cls.conexao:

            return (
                False,
                "Nenhuma conexão ativa."
            )

        try:

            cursor = cls.conexao.cursor()

            cursor.execute(sql)

            try:

                resultados = (
                    cursor.fetchall()
                )

                return (
                    True,
                    resultados
                )

            except:

                cls.conexao.commit()

                return (
                    True,
                    "Comando executado com sucesso."
                )

        except Exception as erro:

            return (
                False,
                str(erro)
            )