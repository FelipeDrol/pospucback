from pydantic import BaseModel
from typing import List
from model.secao import Secao

class SecaoViewSchema(BaseModel):
    """ 
    Define como uma nova seção a ser inserida deve ser representada
    """
    nome: str = "Um nome para agrupar os documentos"

class ListagemSecoesSchema(BaseModel):
    """ 
    Define como uma listagem de seções será retornada
    """
    secoes:List[SecaoViewSchema]

class SecaoEditSchema(BaseModel):
    """ 
    Define como um seção deve ser editada
    """
    id: int = 1
    nome: str = "Um nome para agrupar os documentos"

class SecaoBuscaIdSchema(BaseModel):
    """ 
    Define como deve ser a estrutura que representa a busca. Que será feita apenas com base no id da seção
    """
    id: int = 1

def apresenta_secoes(secoes: List[Secao]):
    """ 
    Retorna varias seções
    """
    result = []
    for secao in secoes:
        result.append({
            "id": secao.id,
            "nome": secao.nome
        })

    return {"secoes": result}

def apresenta_secao(secao: Secao):
    """ 
    Retorna uma seção
    """
    return {
        "id": secao.id,
        "nome": secao.nome
    }
