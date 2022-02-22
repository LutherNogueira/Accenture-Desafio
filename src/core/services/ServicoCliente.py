from typing import Iterable
from models.Cliente import Cliente

class ServicoCliente(): #classe base/ classe pai 
    #os metodos são herdados pelos filhos
    def ler(self) -> Iterable[Cliente]: #ler os dados do csv, instancia, e armazenar no yielt e "retorna" o yielt 
        raise NotImplementedError() #nao ta implementado o metodo --> pq vai ser implementado nos filhos

    def escrever(self,clientes:Iterable[Cliente]): #recebe  o yielt, e vai iterar (FOR) e vai salvar no banco de dados
        raise NotImplementedError() 