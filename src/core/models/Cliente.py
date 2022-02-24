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
    def dadoBruto(cls,dado):
        return cls(
            id=dado['id'],
            nome=dado['nome'],
            email=dado['email'],
            data_cadastro= str(Timestamp(dado['data_cadastro']).to_pydatetime()),
            telefone=dado['telefone']
        )