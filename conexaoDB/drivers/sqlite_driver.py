from conexaoDB.drivers.driver_base import DriverBase


class SqliteDriver(DriverBase):

    def get_connection_fields(self):

        return [
            "Arquivo"
        ]

    def connect(
        self,
        dados
    ):

        arquivo = dados["Arquivo"]

        print(
            f"Abrindo SQLite: {arquivo}"
        )

        return "sqlite_connection"

    def disconnect(
        self,
        conexao
    ):

        print(
            "Desconectando SQLite"
        )