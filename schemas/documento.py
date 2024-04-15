from pydantic import BaseModel
from typing import List
from model.documento import Documento

class DocumentoViewSchema(BaseModel):
    """ 
    Define como um novo documento a ser inserida deve ser representado
    """
    nome: str = "RG"
    secao_id: int = 1


class ListagemDocumentosSchema(BaseModel):
    """ 
    Define como uma listagem de Documentos será retornada
    """
    usuarios:List[DocumentoViewSchema]

class DocumentoEditSchema(BaseModel):
    """ 
    Define como um documento deve ser editado
    """
    nome: str = "RG"
    secao_id: int = 1
    id: int = 1

class DocumentoBuscaIdSchema(BaseModel):
    """ 
    Define como deve ser a estrutura que representa a busca. Que será feita apenas com base no id do Documento
    """
    id: int = 1

class DocumentoBuscaSecaoSchema(BaseModel):
    """ 
    Define como deve ser a estrutura que representa a busca. Que será feita apenas com base no secao_id do Documento
    """
    secao_id: int = 1

def apresenta_documentos(documentos: List[Documento]):
    """ 
    Retorna todos os documentos
    """
    result = []
    for documento in documentos:
        result.append({
            "id": documento.id,
            "nome": documento.nome,
            "secao_id": documento.secao_id,
            "data_insercao": documento.data_insercao
        })

    return {"documentos": result}

def apresenta_documento(documento: Documento):
    """ 
    Retorna um documento
    """
    return {
            "id": documento.id,
            "nome": documento.nome,
            "secao_id": documento.secao_id,
            "data_insercao": documento.data_insercao
        }