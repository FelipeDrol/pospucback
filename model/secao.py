from sqlalchemy import Column, String, Integer, DateTime
from datetime import datetime
from typing import Union

from  model import Base

class Secao(Base):
    __tablename__ = 'secoes'

    id = Column("pk_secao", Integer, primary_key=True)
    nome = Column(String(140), unique=True)
    data_insercao = Column(DateTime, default=datetime.now())

    def __init__(self, nome:str, data_insercao:Union[DateTime, None] = None):
        """
        Cria uma Seção

        Arguments:
            nome: Nome da seção
            data_insercao: Data de quando a secão foi inserida à base
        """
        self.nome = nome

        if data_insercao:
            self.data_insercao = data_insercao

