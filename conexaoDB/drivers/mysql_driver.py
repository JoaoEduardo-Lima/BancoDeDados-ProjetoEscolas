from conexaoDB.drivers.driver_base import DriverBase


class MysqlDriver(DriverBase):

    def get_connection_fields(self):

        return [
            "Host",
            "Porta",
            "Banco",
            "Usuário",
            "Senha"
        ]

    def connect(
        self,
        dados
    ):

        host = dados["Host"]
        porta = dados["Porta"]
        banco = dados["Banco"]
        usuario = dados["Usuário"]
        senha = dados["Senha"]

        print(
            f"Conectando MySQL em {host}:{porta}"
        )

        print(
            f"Banco: {banco}"
        )

        return "mysql_connection"

    def disconnect(
        self,
        conexao
    ):

        print(
            "Desconectando MySQL"
        )