from typing import Iterable
from models.Transacao import Transacao

class ServicoTransacao(): #classe base, classe pai
    def ler(self) -> Iterable[Transacao]:#ler os dados do csv, instancia, e armazenar no yielt e "retorna" o yielt 
        raise NotImplementedError() #nao ta implementado o metodo --> pq vai ser implementado nos filhos

    def escrever(self,transacoes:Iterable[Transacao]): #recebe  o yielt, e vai iterar (FOR) e vai salvar no banco de dados
        raise NotImplementedError()