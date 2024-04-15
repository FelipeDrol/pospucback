from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from datetime import datetime
from typing import Union

from  model import Base

class Documento(Base):
    __tablename__ = 'documentos'

    id = Column("pk_documento", Integer, primary_key=True)
    secao_id = Column(Integer, ForeignKey("secoes.pk_secao"), nullable=False)
    nome = Column(String(140), unique=True)
    data_insercao = Column(DateTime, default=datetime.now())

    def __init__(self, nome:str, secao_id:int, data_insercao:Union[DateTime, None] = None):
        """
        Cria um Documento

        Arguments:
            nome: Nome do documento
            secao_id: Id da seção a qual o documento fará parte
            data_insercao: Data de quando o documento foi inserido à base
        """
        self.nome = nome
        self.secao_id = secao_id

        if data_insercao:
            self.data_insercao = data_insercao

