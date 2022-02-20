from dataclasses import dataclass
from sqlite3 import Date
from Cliente import Cliente

@dataclass
class Transacao:
    id: int
    id_cliente: Cliente
    valor: float
    data: Date
