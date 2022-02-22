
import csv
from typing import Callable, Iterable
from models.Cliente import Cliente
from services.ServicoCliente import ServicoCliente

#cliente local esta relacionado com o que acontece localmente --> nossa maquina = no caso o CSV que esta sendo lido
class ServicoClienteLocal(ServicoCliente): #classe filho da Servico cliente
    def __init__(self,arquivo):
        self.arquivo = arquivo
        self.len = 0 #a ideia é indicar o comprimento do yield

    def ler(self):
        with open(self.arquivo,'r',encoding='utf-8') as dado: #open abre arquivo linha por linha
            for linha in csv.DictReader(dado,delimiter=';',quoting=csv.QUOTE_NONE): #csv dict reader: transforma nosso csv num dicionario de python
                try:
                    cliente=Cliente.dadoBruto(linha)
                    yield cliente #guarda dentro do yield (é quase uma lista que se limpa sozinha e que só existe dentro do método)
                    self.len += 1 
                except Exception as erro:
                    raise Exception(f'Erro na linha => {linha} ',erro)
        print(f"Os {self.len} registros dos clientes foram salvos com sucesso")