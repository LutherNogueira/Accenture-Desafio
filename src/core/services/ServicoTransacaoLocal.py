import csv
from typing import Callable, Iterable
from models.Transacao import Transacao
from services.ServicoTransacao import ServicoTransacao

class ServicoTransacaoLocal(ServicoTransacao):
    def __init__(self,arquivo):
        self.arquivo = arquivo

    def ler(self):
        with open(self.arquivo,'r',encoding='utf-8') as dado:
            for linha in csv.DictReader(dado,delimiter=';',quoting=csv.QUOTE_NONE):
                try:
                    transacao=Transacao.dadoBruto(linha)
                    yield transacao
                except Exception as erro:
                    raise Exception(f'Erro na linha => {linha} ',erro)