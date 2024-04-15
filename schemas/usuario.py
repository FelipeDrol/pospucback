from pydantic import BaseModel
from typing import List
from model.usuario import Usuario

class UsuarioViewSchema(BaseModel):
    """ 
    Define como um novo usuário a ser inserido deve ser representado
    """
    nome: str = "Nome Sobrenome"
    email: str = "nome.sobrenome@email.com"
    administrador: bool = False

class ListagemUsuariosSchema(BaseModel):
    """ 
    Define como uma listagem de usuários será retornada
    """
    usuarios:List[UsuarioViewSchema]

class UsuarioEditSchema(BaseModel):
    """ 
    Define como um Usuário deve ser editado
    """
    nome: str = "Nome Sobrenome"
    email: str = "nome.sobrenome@email.com"
    administrador: bool = False
    id: int = 1

class UsuarioBuscaEmailSchema(BaseModel):
    """ 
    Define como deve ser a estrutura que representa a busca. Que será feita apenas com base no email do Usuário
    """
    email: str = "nome.sobrenome@email.com"

class UsuarioBuscaIdSchema(BaseModel):
    """ 
    Define como deve ser a estrutura que representa a busca. Que será feita apenas com base no id do Usuário
    """
    id: int = 1

def apresenta_usuarios(usuarios: List[Usuario]):
    """ 
    Retorna varios usuários
    """
    result = []
    for usuario in usuarios:
        result.append({
            "id": usuario.id,
            "nome": usuario.nome,
            "email": usuario.email,
            "administrador": usuario.administrador
        })

    return {"usuarios": result}

def apresenta_usuario(usuario: Usuario):
    """ 
    Retorna um usuário
    """
    return {
        "id": usuario.id,
        "nome": usuario.nome,
        "email": usuario.email,
        "administrador": usuario.administrador
    }

def apresenta_primeiro_usuario(administrador: bool):
    """ 
    Retorna uma representação do Usuário para primeiro acesso ou Usuário nao localizado
    """
    return {
        "id": "",
        "nome": "",
        "email": "",
        "administrador": administrador
    }