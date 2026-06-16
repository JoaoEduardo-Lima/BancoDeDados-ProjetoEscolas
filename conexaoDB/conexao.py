class GerenciadorBancoDeDados:

    current_driver = None

    current_name = "Nenhum"

    @classmethod
    def set_driver(
        cls,
        driver,
        name
    ):

        cls.current_driver = driver
        cls.current_name = name

    @classmethod
    def connect(cls):

        if cls.current_driver:

            cls.current_driver.connect()

    @classmethod
    def disconnect(cls):

        if cls.current_driver:

            cls.current_driver.disconnect()