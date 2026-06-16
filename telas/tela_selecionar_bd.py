from core.menu import Menu

from conexaoDB.conexao import GerenciadorBancoDeDados
from conexaoDB.drivers.sqlserver_driver import SqlServerDriver
from conexaoDB.drivers.mysql_driver import MysqlDriver
from conexaoDB.drivers.postgres_driver import PostgresDriver
from conexaoDB.drivers.sqlite_driver import SqliteDriver



class Tela_SelecionarSGBD(Menu):

    def __init__(self, master, app):

        options = [
            ("Voltar",self.voltar),
            ("SQL Server",self.sqlserver),
            ("MySQL",self.mysql),
            ("PostgreSQL",self.postgresql),
            ("SQLite",self.sqlite)
        ]

        super().__init__(
            master,
            app,
            "Selecionar SGBD",
            options,
            subtitle=f"Banco Atual: {GerenciadorBancoDeDados.current_name}"
        )

    def sqlserver(self):

        GerenciadorBancoDeDados.set_driver(
            SqlServerDriver(),
            "SQL Server"
        )
        self.recarregar()

    def mysql(self):
        
        GerenciadorBancoDeDados.set_driver(
            MysqlDriver(),
            "MySQL Server"
        )
        self.recarregar()

    def postgresql(self):
       
        GerenciadorBancoDeDados.set_driver(
            PostgresDriver(),
            "PostGreSQL Server"
        )
        self.recarregar()

    def sqlite(self):
               
        GerenciadorBancoDeDados.set_driver(
            SqliteDriver(),
            "SQLite Server"
        )
        self.recarregar()
        
    def voltar(self):

        self.app.go_back()

    def recarregar(self):

        self.app.refresh_screen()