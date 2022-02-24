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

        print("7 - Imprimir na tela modelo de importação")
        print("8 - Sair")
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
            print("Header de importação do cliente:id;nome;email;data_cadastro;telefone ")
            print(" id: int \n nome: str\n email: str \n data_cadastro: datetimeoffset \n telefone str")
            print("Header de importação do transacao:id;cliente_id;valor;data \n")
            print(" id: int \n cliente_id: int \n valor: float \n data: datetimeoffset\n")
            
            print("Atenção:\n- O formato deve ser csv separado por ponto e vírgula. \n- O header deve constar somente no primeiro arquivo \n")
            print("Nome do arquivo: (O xxx deve ser substituido pelo número do arquivo. Iniciando obrigatóriamente em 001)\n - Cliente: clients-xxx.csv\n - Transacao IN: transaction-in-xxx.csv\n - Transacao IN: transaction-out-xxx.csv")
        elif opcao == 8:
            break
        else:
            print("\nOpção inválida\n")
