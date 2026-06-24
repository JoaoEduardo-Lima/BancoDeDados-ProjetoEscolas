from conexaoDB.conexao import GerenciadorBancoDeDados

class QueryExecutor:

    @staticmethod
    def executar(sql):

        return (
            GerenciadorBancoDeDados
            .execute(sql)
        )