# BancoDeDados-ProjetoEscolas

Sistema desktop desenvolvido em Python com Tkinter para gerenciamento e interação com diferentes Sistemas Gerenciadores de Banco de Dados (SGBDs).

O projeto foi criado com foco em modularização, navegação por menus e suporte a múltiplos bancos de dados, permitindo que novas funcionalidades sejam adicionadas facilmente.

---

## Funcionalidades Atuais

### Interface

- Navegação por teclado
  - ↑ Mover para cima
  - ↓ Mover para baixo
  - ENTER Selecionar opção
- Histórico de telas
- Troca de resolução da janela
- Sistema de temas
  - Tema Escuro
  - Tema Claro
  - Tema Pastel
- Centralização automática da janela

### Banco de Dados

- Seleção de SGBD
  - SQL Server
  - MySQL
  - PostgreSQL
  - SQLite
- Configuração dinâmica de conexão
- Campos de conexão gerados automaticamente conforme o banco escolhido
- Teste de conexão
- Exibição de mensagens de sucesso ou erro na interface

---

## Estrutura do Projeto

```text
BancoDeDados-ProjetoEscolas/

├── main.py

├── core/
│   ├── janela.py
│   ├── menu.py
│   └── input.py

├── telas/
│   ├── tela_inicial.py
│   ├── tela_configuracao.py
│   ├── tela_bancodedados.py
│   ├── tela_selecionar_bd.py
│   ├── tela_config_bd.py
│   ├── tela_resolucao.py
│   └── tela_tema.py

├── UI/
│   ├── tema.py
│   ├── gerenciador_tema.py
│   ├── estilo.py
│   └── animacao.py

├── conexaoDB/
│   ├── conexao.py
│   └── drivers/
│       ├── driver_base.py
│       ├── sqlserver_driver.py
│       ├── mysql_driver.py
│       ├── postgres_driver.py
│       └── sqlite_driver.py

└── README.md
```

---

## Tecnologias Utilizadas

- Python 3.13
- Tkinter
- PyODBC
- SQLite3
- SQL Server Express

---

## Instalação

Clone o repositório:

```bash
git clone https://github.com/seu-usuario/BancoDeDados-ProjetoEscolas.git
```

Entre na pasta:

```bash
cd BancoDeDados-ProjetoEscolas
```

Instale as dependências:

```bash
pip install pyodbc
```

---

## Executando

```bash
py main.py
```

---

## Configuração SQL Server

Exemplo:

```text
Servidor:
localhost\SQLEXPRESS

Banco:
MaquinasPadilha
```

O sistema utiliza autenticação integrada do Windows:

```python
Trusted_Connection=yes
```

---

## Objetivos Futuros

### CRUD Completo

- Criar registros
- Ler registros
- Atualizar registros
- Excluir registros

### Ferramentas SQL

- Executar consultas SQL
- Exibir resultados em tabelas
- Exportar resultados
- Histórico de comandos SQL

### Administração

- Listar bancos de dados
- Listar tabelas
- Visualizar estrutura de tabelas
- Criar tabelas
- Alterar tabelas

### Persistência

- Salvar configurações em arquivo
- Restaurar tema selecionado
- Restaurar resolução escolhida
- Restaurar último banco configurado

---

## Arquitetura

O projeto segue uma arquitetura baseada em:

- Separação por responsabilidades
- Componentes reutilizáveis
- Menus genéricos
- Drivers independentes para cada SGBD
- Fácil expansão para novos bancos de dados

---

## Autor

João Eduardo

Projeto desenvolvido para estudo de Python, Tkinter e Sistemas Gerenciadores de Banco de Dados.