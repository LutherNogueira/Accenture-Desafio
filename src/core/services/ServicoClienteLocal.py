
import csv
from typing import Callable, Iterable
from src.core.models.Cliente import Cliente
from src.core.services.ServicoCliente import ServicoCliente

class ServicoClienteLocal(ServicoCliente):
    def __init__(self,dado):
        self.dado = dado

    def ler(self):
        for linha in csv.DictReader(self.dado,delimiter=';',quoting=csv.QUOTE_NONE):
            try:
                cliente=Cliente.dadoBruto(linha)
                yield cliente
            except Exception as erro:
                raise Exception(f'Erro na linha => {linha} ',erro)
    def sumarizar():
        pass