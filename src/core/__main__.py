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

        if opcao == 1:  # Conectar banco de dados
            ServiceODBC.testConnection()
        elif opcao == 2:  # Criar estruturas de tabela
            ServiceDados.criarTabelasDB()
        elif opcao == 3: # Apagar todos as tabelas do Banco de dados
            ServiceODBC.dropAllTables()
        elif opcao == 4:  # Carregar dados do CSV
             ServiceDados.carregareMigrar()
        elif opcao == 5:  # Sumarizar dados salvos no Banco de dados
            ServiceDados.sumarizarDB()
        elif opcao == 6:  # Apagar todos os dados do Banco de dados
            ServiceODBC.deleteAllTables()
        elif opcao == 7:
            break
        else:
            print("\nOpção inválida\n")
