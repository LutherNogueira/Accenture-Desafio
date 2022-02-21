
import csv
from typing import Callable, Iterable
from models.Cliente import Cliente
from services.ServicoCliente import ServicoCliente

class ServicoClienteLocal(ServicoCliente):
    def __init__(self,arquivo):
        self.arquivo = arquivo

    def ler(self):
        with open(self.arquivo,'r',encoding='utf-8') as dado:
            for linha in csv.DictReader(dado,delimiter=';',quoting=csv.QUOTE_NONE):
                try:
                    cliente=Cliente.dadoBruto(linha)
                    yield cliente
                except Exception as erro:
                    raise Exception(f'Erro na linha => {linha} ',erro)