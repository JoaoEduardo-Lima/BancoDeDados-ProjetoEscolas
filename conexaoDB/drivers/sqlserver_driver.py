import pyodbc

from conexaoDB.drivers.driver_base import DriverBase


class SqlServerDriver(DriverBase):

    def get_connection_fields(self):

        return [
            "Servidor",
            "Banco"
        ]

    def connect(
        self,
        dados
    ):

        servidor = dados["Servidor"]
        banco = dados["Banco"]

        conexao = pyodbc.connect(

            f"""
            DRIVER={{SQL Server}};
            SERVER={servidor};
            DATABASE={banco};
            Trusted_Connection=yes;
            """
        )

        return conexao

    def disconnect(
        self,
        conexao
    ):

        conexao.close()
