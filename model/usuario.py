from sqlalchemy import Column, String, Integer, Boolean, DateTime
from datetime import datetime
from typing import Union

from  model import Base

class Usuario(Base):
    __tablename__ = 'usuarios'

    id = Column("pk_usuario", Integer, primary_key=True)
    nome = Column(String(140))
    email = Column(String(140), unique=True)
    administrador = Column(Boolean)
    data_insercao = Column(DateTime, default=datetime.now())

    def __init__(self, nome:str, email:str,administrador:bool, data_insercao:Union[DateTime, None] = None):
        """
        Cria um Usuário

        Arguments:
            nome: Nome do Usuário
            email: E-mail do Usuário
            administrador: Campo booleano que define se o Usuário será administrador
            data_insercao: Data de quando o Usuário foi inserido à base
        """
        self.nome = nome
        self.email = email
        self.administrador = administrador

        if data_insercao:
            self.data_insercao = data_insercao
