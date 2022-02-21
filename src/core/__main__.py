from services.ServiceDados import ServiceDados
from services.ServicoODBC import ServiceODBC

if __name__ == "__main__":

    while True:
        print("--------------------------------------------------")
        print("1 - Testar conexão com banco de dados")
        print("2 - Criar estruturas de tabela no banco de dados")
        print("3 - Apagar todos as tabelas do Banco de dados\n")

        print("4 - Carregar dados via csv e iniciar migração para banco de dados\n")

        print("5 - Sumarizar dados salvos no Banco de dados")
        print("6 - Apagar todos os dados do Banco de dados")

        print("7 - Sair")
        print("--------------------------------------------------")

        opcao = int(input())

        match opcao:
            case 1:  # Conectar banco de dados
                ServiceODBC.testConnection()
            case 2:  # Criar estruturas de tabela
                ServiceDados.criarTabelasDB()
            case 3: # Apagar todos as tabelas do Banco de dados
                ServiceODBC.dropAllTables()
            case 4:  # Carregar dados do CSV
                 ServiceDados.carregareMigrar()
            case 5:  # Sumarizar dados salvos no Banco de dados
                ServiceDados.sumarizarDB()
            case 6:  # Apagar todos os dados do Banco de dados
                ServiceODBC.deleteAllTables()
            case 7:
                break
            case _:
                print("\nOpção inválida\n")
