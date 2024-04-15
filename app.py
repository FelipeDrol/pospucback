from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect
from sqlalchemy.exc import IntegrityError
from model import Session, Usuario, Secao, Documento
from logger import logger
from schemas import *
from flask_cors import CORS

info = Info(title="API de Documentos", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

home_tag = Tag(name="Documentação", description="Seleção de documentação: Swagger, Redoc ou RapiDoc")
usuario_tag = Tag(name="Usuário", description="Visualização, Adição, edição e remoção de usuários à base")
secao_tag = Tag(name="Seção", description="Visualização, Adição, edição e remoção de seções à base")
documento_tag = Tag(name="Documento", description="Visualização, Adição, edição e remoção de documentos à base")

#Metodos Gerais
def get_todos_usuario():
    return Session().query(Usuario).all()

def get_todas_secoes():
    return Session().query(Secao).all()

def get_todos_documentos():
    return Session().query(Documento).all()

def retornos_listagem_usuarios():
    return {"200": ListagemUsuariosSchema, "400": ErrorSchema, "404": ErrorSchema}

def retornos_usuario_view():
    return {"200": UsuarioViewSchema, "400": ErrorSchema, "404": ErrorSchema}

def retornos_listagem_secoes():
    return {"200": ListagemSecoesSchema, "400": ErrorSchema, "404": ErrorSchema}

def retornos_secao_view():
    return {"200": SecaoViewSchema, "400": ErrorSchema, "404": ErrorSchema}

def retornos_listagem_documentos():
    return {"200": ListagemDocumentosSchema, "400": ErrorSchema, "404": ErrorSchema}

def retornos_documento_view():
    return {"200": DocumentoViewSchema, "400": ErrorSchema, "404": ErrorSchema}

def retorno_erro(e, mensagem, code):
    logger.warning(e)
    error_msg = mensagem + ": " + repr(e)
    return {"message": error_msg}, code

#Apis Home
@app.get('/', tags=[home_tag])
def home():
    """
    Redireciona para /openapi, tela que permite a escolha do estilo de documentação.
    """
    return redirect('/openapi')

#Apis usuários
@app.get('/usuarios', tags=[usuario_tag], responses = retornos_listagem_usuarios())
def get_usuarios():
    """
    Retorna todos os usuários cadastrados, sem criterios de busca
    """
    try:
        usuarios = get_todos_usuario()
        return apresenta_usuarios(usuarios), 200
    except Exception as e:
        retorno_erro(e, "Não foi possível obter os usuários", 400)
    
@app.get('/usuario', tags=[usuario_tag], responses = retornos_usuario_view())
def get_usuario(query: UsuarioBuscaEmailSchema):
    """
    Retorna um usuário pelo seu e-mail
    """
    try:
        session = Session()
        usuario = session.query(Usuario).filter(Usuario.email == query.email).first()
        if(usuario):
            return apresenta_usuario(usuario), 200
        else:
            administrador = False
            if(len(get_todos_usuario()) < 1):
                administrador = True
            return apresenta_primeiro_usuario(administrador), 200
    except Exception as e:
        retorno_erro(e, "Não foi possível obter o usuário", 400)
    
@app.post('/usuario', tags=[usuario_tag], responses = retornos_listagem_usuarios())
def add_usuario(form: UsuarioViewSchema):
    """
    Adiciona um novo usuário à base
    Retorna todos os usuários cadastrados
    """
    try:
        usuario = Usuario(nome=form.nome, email=form.email, administrador=form.administrador)
        session = Session()
        session.add(usuario)
        session.commit()

        usuarios = get_todos_usuario()
        return apresenta_usuarios(usuarios), 200
    except IntegrityError as e:
        retorno_erro(e, "Usuário de mesmo nome já salvo na base", 409)
    except Exception as e:
        retorno_erro(e, "Não foi possível adicionar o usuário", 400)

@app.delete('/usuario', tags=[usuario_tag], responses = retornos_listagem_usuarios())
def del_usuario(query: UsuarioBuscaIdSchema):
    """
    Deleta um usuário a partir do seu id
    Retorna todos os usuários cadastrados
    """
    try:
        session = Session()
        sqlQuery = session.query(Usuario).filter(Usuario.id == query.id)
        usuario = sqlQuery.first()
        if(usuario):
            sqlQuery.delete()
            session.commit()
            usuarios = get_todos_usuario()
            return apresenta_usuarios(usuarios), 200
        else:
            return {"message": "Usuário não localizado"}, 404
    except Exception as e:
        retorno_erro(e, "Erro ao deletar usuário", 400)

@app.get('/usuariobyid', tags=[usuario_tag], responses = retornos_usuario_view())
def get_usuarioById(query: UsuarioBuscaIdSchema):
    """
    Retorna um usuário pelo seu id
    """
    try:
        usuario = Session().query(Usuario).filter(Usuario.id == query.id).first()
        if(usuario):
            return apresenta_usuario(usuario), 200
        else:
            return {"message": "Usuário não localizado"}, 404
    except Exception as e:
        retorno_erro(e, "Erro ao buscar usuário", 400)
    
@app.post('/editarusuario', tags=[usuario_tag], responses = retornos_listagem_usuarios())
def edit_usuario(form: UsuarioEditSchema):
    """
    Edita um usuário existente pelo seu id
    Retorna todos os usuários cadastrados
    """
    try:
        session = Session()
        usuario = session.query(Usuario).filter(Usuario.id == form.id).first()
        if(usuario):
            usuario.nome = form.nome
            usuario.email = form.email
            usuario.administrador = form.administrador
            session.commit()
            usuarios = usuarios = get_todos_usuario()
            return apresenta_usuarios(usuarios), 200
        else:
            return {"message": "Usuário não localizado"}, 404
    except Exception as e:
        retorno_erro(e, "Não foi possível editar o usuário", 400)

#Apis Seções
@app.get('/secoes', tags=[secao_tag], responses = retornos_listagem_secoes())
def get_secoes():
    """
    Retorna todas as seções cadastradas
    """
    try:
        secoes = get_todas_secoes()
        return apresenta_secoes(secoes), 200
    except Exception as e:
        retorno_erro(e, "Erro ao buscar todas as seções", 400)

@app.get('/secao', tags=[secao_tag],responses = retornos_secao_view())
def get_secaoId(query: SecaoBuscaIdSchema):
    """
    Retorna uma seção pelo seu id
    """
    try:
        secao = Session().query(Secao).filter(Secao.id == query.id).first()
        if(secao):
            return apresenta_secao(secao), 200
        else:
            return {"message": "Seção não localizada"}, 404
    except Exception as e:
        retorno_erro(e, "Erro ao buscar a seção", 400)
    
@app.post('/secao', tags=[secao_tag], responses = retornos_listagem_secoes())
def add_secao(form: SecaoViewSchema):
    """
    Adiciona uma seção à base
    Retorna todas as seções cadastradas
    """
    try:
        secao = Secao(nome=form.nome)
        session = Session()
        session.add(secao)
        session.commit()

        secoes = get_todas_secoes()
        return apresenta_secoes(secoes), 200
    except IntegrityError as e:
        retorno_erro(e, "Seção de mesmo nome já salvo na base", 409)
    except Exception as e:
        retorno_erro(e, "Não foi possível adicionar a nova seção", 400)

@app.delete('/secao', tags=[secao_tag], responses = retornos_listagem_secoes())
def del_secao(query: SecaoBuscaIdSchema):
    """
    Deleta uma seção a partir do seu id
    Retorna todas as seções cadastradas
    """
    try:
        session = Session()
        sqlQuery = session.query(Secao).filter(Secao.id == query.id)
        secao = sqlQuery.first()
        if(secao):
            sqlQuery.delete()
            session.commit()
            secoes = get_todas_secoes()
            return apresenta_secoes(secoes), 200
        else:
            return {"message": "Seção não localizada"}, 404
    except Exception as e:
        retorno_erro(e, "Erro ao deletar seção", 400)
    
@app.post('/editarsecao', tags=[secao_tag], responses = retornos_listagem_secoes())
def edit_secao(form: SecaoEditSchema):
    """
    Edita um seção existente pelo seu id
    Retorna todas as seções cadastradas
    """
    try:
        session = Session()
        secao = session.query(Secao).filter(Secao.id == form.id).first()
        if(secao):
            secao.nome = form.nome
            session.commit()
            secoes = get_todas_secoes()
            return apresenta_secoes(secoes), 200
        else:
            return {"message": "Seção não localizada"}, 404
    except Exception as e:
        retorno_erro(e, "Erro ao editar seção", 400)
        error_msg = ": " + repr(e)
    
#Apis Envio de arquivos
@app.get('/documentos', tags=[documento_tag], responses = retornos_listagem_documentos())
def get_documentos(query: DocumentoBuscaSecaoSchema):
    """
    Retorna todos os documentos cadastrados por id da seção
    """
    try:
        documentos = Session().query(Documento).filter(Documento.secao_id == query.secao_id).all()
        return apresenta_documentos(documentos), 200
    except Exception as e:
        retorno_erro(e, "Não foi possível obter o usuário", 400)
        error_msg = "Erro ao buscar todos os documentos por id da seção: " + repr(e)    

@app.get('/documento', tags=[documento_tag], responses = retornos_documento_view())
def get_documento(query: DocumentoBuscaIdSchema):
    """
    Retorna um Documento a partir do seu id
    """
    try:
        documento = Session().query(Documento).filter(Documento.id == query.id).first()
        if(documento):
            return apresenta_documento(documento), 200
        else:
            return {"message": "Documento não localizado"}, 404
    except Exception as e:
        retorno_erro(e, "Erro ao obter documento por id", 400)
    
@app.post('/documento', tags=[documento_tag], responses = retornos_listagem_documentos())
def add_documento(form: DocumentoViewSchema):
    """
    Adiciona um novo documento à base
    Retorna todos os documentos cadastrados
    """
    try:
        documento = Documento(nome=form.nome, secao_id = form.secao_id)
        session = Session()
        session.add(documento)
        session.commit()

        documentos = get_todos_documentos()
        return apresenta_documentos(documentos), 200
    except Exception as e:
        retorno_erro(e, "Não foi possível obter o usuário", 400)
        error_msg = "Não foi possível adicionar o novo documento:" + repr(e)

@app.delete('/documento', tags=[documento_tag], responses = retornos_listagem_documentos())
def del_documento(query: DocumentoBuscaIdSchema):
    """
    Deleta um documento a partir do seu id
    Retorna todos os documentos cadastrados
    """
    try:
        session = Session()
        sqlQuery = session.query(Documento).filter(Documento.id == query.id)
        documento = sqlQuery.first()
        if(documento):
            sqlQuery.delete()
            session.commit()
            documentos = get_todos_documentos()
            return apresenta_documentos(documentos), 200
        else:
            return {"message": "Documento não localizado"}, 404
    except Exception as e:
        retorno_erro(e, "Não foi possível obter o usuário")
        error_msg = "Erro ao deletar documento: " + repr(e)
        return {"message": error_msg}, 404
    
@app.post('/editardocumento', tags=[documento_tag], responses = retornos_listagem_documentos())
def edit_documento(form: DocumentoEditSchema):
    """
    Edita um documento existente pelo seu id
    Retorna todos os documentos cadastrados
    """
    try:
        session = Session()
        documento = session.query(Documento).filter(Documento.id == form.id).first()
        if(documento):
            documento.nome = form.nome
            documento.secao_id = form.secao_id
            session.commit()
            documentos = get_todos_documentos()
            return apresenta_documentos(documentos), 200
        else:
            return {"message": "Documento não localizado"}, 404
    except Exception as e:
        retorno_erro(e, "Erro ao editar Documento")