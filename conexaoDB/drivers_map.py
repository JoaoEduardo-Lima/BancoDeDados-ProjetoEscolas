from conexaoDB.drivers.sqlserver_driver import SqlServerDriver
from conexaoDB.drivers.mysql_driver import MysqlDriver
from conexaoDB.drivers.postgres_driver import PostgresDriver
from conexaoDB.drivers.sqlite_driver import SqliteDriver


DRIVERS = {

    "SQL Server":
        SqlServerDriver,

    "MySQL Server":
        MysqlDriver,

    "PostGreSQL Server":
        PostgresDriver,

    "SQLite Server":
        SqliteDriver
}