class DriverBase:

    def get_connection_fields(self):

        raise NotImplementedError

    def connect(
        self,
        dados
    ):

        raise NotImplementedError

    def disconnect(
        self,
        conexao
    ):

        raise NotImplementedError