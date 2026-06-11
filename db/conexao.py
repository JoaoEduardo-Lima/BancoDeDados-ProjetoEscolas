import pyodbc

server = 'localhost\\SQLEXPRESS01'
database = 'MaquinasPadilha'

conn_str = f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;'

def conectar():
    try:
        return pyodbc.connect(conn_str)
    except Exception as e:
        print("Erro conexão:", e)
        return None
    
conn = conectar()
if conn:
    cursor = conn.cursor()

    #vercel