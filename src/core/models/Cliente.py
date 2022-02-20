from dataclasses import dataclass
from sqlite3 import Date

@dataclass
class Cliente:
    id: int
    nome: str
    email: str
    data_cadastro: Date
    telefone: str
