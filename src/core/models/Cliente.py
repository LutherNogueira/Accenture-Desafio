from dataclasses import dataclass
from datetime import datetime
from pandas import Timestamp 

@dataclass
class Cliente:
    id: int
    nome: str
    email: str
    data_cadastro: datetime
    telefone: str

    @classmethod
    def dadoBruto(cls,dado): #as chaves do dcionario sao o header do csv 
        return cls(  #retonando uma instnacia de cliente a partir de uma linha de dado do CSV
            id=dado['id'],
            nome=dado['nome'],
            email=dado['email'],
            data_cadastro= str(Timestamp(dado['data_cadastro']).to_pydatetime()), #convertendo o data,
            #horário e time zone pra timestamp do pandas e convertendo pro formato datetime do python e
            #  depois cnvertendo pra string
            telefone=dado['telefone']
        )

        #data_cadastro = datetime.strptime(dado['data_cadastro'],'%Y-%m-%d %H:%M:%S %z'),