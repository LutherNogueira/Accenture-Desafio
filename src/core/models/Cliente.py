from dataclasses import dataclass
from datetime import datetime
from pandas import Timestamp as pd

@dataclass
class Cliente:
    id: int
    nome: str
    email: str
    data_cadastro: datetime
    telefone: str

    @classmethod
    def dadoBruto(cls,dado):
        return cls(
            id=dado['id'],
            nome=dado['nome'],
            email=dado['email'],
            data_cadastro= str(pd(dado['data_cadastro']).to_pydatetime()),
            #data_cadastro = datetime.strptime(dado['data_cadastro'],'%Y-%m-%d %H:%M:%S %z'),
            telefone=dado['telefone']
        )
