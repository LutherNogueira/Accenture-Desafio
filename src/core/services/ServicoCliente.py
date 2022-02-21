from typing import Iterable
from src.core.models.Cliente import Cliente

class ServicoCliente():
    def ler(self) -> Iterable[Cliente]:
        raise NotImplementedError()

    def escrever(self,clientes:Iterable[Cliente]):
        raise NotImplementedError()