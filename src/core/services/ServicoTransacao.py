from typing import Iterable
from models.Transacao import Transacao

class ServicoTransacao():
    def ler(self) -> Iterable[Transacao]:
        raise NotImplementedError()

    def escrever(self,transacoes:Iterable[Transacao]):
        raise NotImplementedError()