from conexaoDB.conexao import GerenciadorBancoDeDados

class SchemaLoader:

    @staticmethod
    def carregar_tabelas():

        sucesso, resultado = (
            GerenciadorBancoDeDados.execute(
                """
                SELECT TABLE_NAME
                FROM INFORMATION_SCHEMA.TABLES
                """
            )
        )

        if not sucesso:

            return []

        return [

            linha[0]

            for linha in
            resultado["linhas"]
        ]