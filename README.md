# API de Documentos

MVP para Disciplina **Desenvolvimento Full Stack Básico** 

O objetivo aqui é ilustrar um exemplo de backend de um painel administrativo de um CMS onde o administrador pode gerar seções com documentos onde um usuário nao administrativo terá de enviar os arquivos solicitados. Atualmente temos somente o administrativo, sem envio de documentos e sem aprovação. A ideia é fazer isto nos proximos MVPs.
No primeiro acesso, o sistema irá aceitar qualquer e-mail

## Como executar 

Será necessário ter todas as libs python listadas no `requirements.txt` instaladas.
Após clonar o repositório, é necessário ir ao diretório raiz, pelo terminal, para poder executar os comandos descritos abaixo.

> É fortemente indicado o uso de ambientes virtuais do tipo [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html).

```
(env)$ pip install -r requirements.txt
```

Este comando instala as dependências/bibliotecas, descritas no arquivo `requirements.txt`.

Para executar a API  basta executar:

```
(env)$ flask run --host 0.0.0.0 --port 5000
```

Abra o [http://localhost:5000/#/](http://localhost:5000/#/) no navegador para verificar o status da API em execução.
