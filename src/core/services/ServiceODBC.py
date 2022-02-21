import pyodbc
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

class ServiceODBC():
    server =os.getenv('SERVER')
    database =os.getenv('DATABASE') 
    username =os.getenv('DBUSERNAME') 
    password =os.getenv('PASSWORD')

    @staticmethod
    def openConnection():
        try:
            conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};  \
                                SERVER='+ServiceODBC.server + ';             \
                                DATABASE='+ServiceODBC.database+';            \
                                UID='+ServiceODBC.username+';                  \
                                PWD=' + ServiceODBC.password)
            return conn
        except pyodbc.Error as e:
            print(f"Erro ao conectar ao banco de dados : {str(e)}")
            
    @staticmethod
    def closeConection(cursor: pyodbc.Cursor, conn: pyodbc.Connection):
        cursor.close()
        conn.close()

    @staticmethod
    def dropAllTables():
        try:
            
            tables = ["TRANSACOES","CLIENTES"]

            
            for item in tables:
                
                if ServiceODBC.checkIfTableExists(item):

                    sqlcommand=f''' 
                        DROP TABLE IF EXISTS {item} CASCADE; 
                    '''
                    conn =ServiceODBC.openConection()
                    conn.cursor().execute(sqlcommand)
                    conn.commit()
                    conn.close()

                    print(f'Tabela {item} foi apagada com sucesso!' )
                else:
                    print(f'Tabela {item} não pode ser apagada' )

        except pyodbc.Error as e:
            print(f"Erro ao apagar dados do banco de dados : {str(e)}")
        except OSError as err:
            print("Erro de Sistema Operacional: {0}".format(err))
        except ValueError:
            print("Não foi possível fazer a conversão de tipo")
        except BaseException as err:
            print(f"Erro inesperado {err=}, {type(err)=}")

    @staticmethod
    def deleteAllTables(tableName):
        try:
            
            tables = ["TRANSACOES","CLIENTES"]
            
            for item in tables:
                
                if ServiceODBC.checkIfTableExists(item):

                    sqlcommand=f''' 
                        DELETE FROM {item} CASCADE; 
                    '''
                    cursor, conn =ServiceODBC.openConection()
                    cursor.execute(sqlcommand)
                    conn.commit()
                    cursor.close()
                    conn.close()

                    print(f'Registros da tabela {item} foram apagados com sucesso!' )
                else:
                    print(f'Registros da tabela  {item} não puderam ser apagados' )

        except pyodbc.Error as e:
            print(f"Erro ao apagar dados do banco de dados : {str(e)}")
        except OSError as err:
            print("Erro de Sistema Operacional: {0}".format(err))
        except ValueError:
            print("Não foi possível fazer a conversão de tipo")
        except BaseException as err:
            print(f"Erro inesperado {err=}, {type(err)=}")

    @staticmethod
    def testConnection():
        try:
            (cursor, conection) = ServiceODBC.openConection()
            if cursor is not None:
                ServiceODBC.closeConection(cursor, conection)
                print("Conexão estabelecida com sucesso")
        except:
            print("Falha em estabelecer conexão com Banco de Dados")

    def checkIfTableExists(table_name):
        try:
            conn =ServiceODBC.openConnection()
            
            sqlcommand=f''' 
                SELECT *
                FROM INFORMATION_SCHEMA.TABLES
                WHERE TABLE_SCHEMA = 'dbo'
                AND TABLE_NAME = '{table_name}'; 
            '''

            conn.cursor().execute(sqlcommand)
            if conn.cursor().rowcount == -1:
                conn.close()
                return False
            else: 
                conn.close()
                return True
            
        except pyodbc.Error as e:
            print(f"Erro ao checar tabela {table_name}: {str(e)}")
        except OSError as err:
            print("Erro de Sistema Operacional: {0}".format(err))
        except ValueError:
            print("Não foi possível fazer a conversão de tipo")
        except BaseException as err:
            print(f"Erro inesperado {err=}, {type(err)=}")
        