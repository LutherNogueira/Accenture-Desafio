import csv
from genericpath import exists
from typing import Callable, Iterable
from models.Transacao import Transacao
from services.ServicoTransacao import ServicoTransacao

#transacao local esta relacionado com o que acontece localmente --> nossa maquina = no caso o CSV que esta sendo lido
class ServicoTransacaoLocal(ServicoTransacao): #classe filho da Servico Transacao
    def __init__(self,arquivo):
        self.arquivo = arquivo
        self.len=0 #a ideia é indicar o comprimento do yield

    def ler(self):
        if not exists(self.arquivo):
            print("Arquivo não encontrado. Revise o nome do arquivo.")
        else:
            print("Arquivo encontrado. Iniciando leitura...")
            with open(self.arquivo,'r',encoding='utf-8') as dado:  #open abre arquivo linha por linha
                for linha in csv.DictReader(dado,delimiter=';',quoting=csv.QUOTE_NONE):  #csv dict reader: transforma nosso csv num dicionario de python
                    try:
                        transacao=Transacao.dadoBruto(linha)
                        yield transacao #guarda dentro do yield (é quase uma lista que se limpa sozinha e que só existe dentro do método)
                        self.len += 1
                    except Exception as erro:
                        raise Exception(f'Erro na linha => {linha} ',erro)
            print(f"Os {self.len} registros das transacoes foram salvos com sucesso")
        