import csv
from genericpath import exists
from typing import Callable, Iterable
from models.Transacao import Transacao
from services.ServicoTransacao import ServicoTransacao

class ServicoTransacaoLocal(ServicoTransacao):
    def __init__(self,arquivo):
        self.arquivo = arquivo
        self.len=0

    def ler(self):
        if not exists(self.arquivo):
            print("Arquivo não encontrado. Revise o nome do arquivo.")
        else:
            print("Arquivo encontrado. Iniciando leitura...")
            with open(self.arquivo,'r',encoding='utf-8') as dado:
                for linha in csv.DictReader(dado,delimiter=';',quoting=csv.QUOTE_NONE):
                    try:
                        transacao=Transacao.dadoBruto(linha)
                        yield transacao
                        self.len += 1
                    except Exception as erro:
                        raise Exception(f'Erro na linha => {linha} ',erro)
            print(f"Os {self.len} registros das transacoes foram salvos com sucesso")
        