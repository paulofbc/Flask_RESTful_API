# API RESTful com Flask e SQLite
Projeto de participação em uma seletiva de estágio para o Cesar Labs. O código consiste em uma API RESTful em Flask com as operações básicas (CRUD) com um banco de dados.

## Para rodar o projeto

Primeiro, baixe as dependências do python através do requirements.txt:
``` sh
$ pip install -r requirements.txt
```

Depois rode a API:
``` sh
$ python api.py
```
Agora o projeto já está rodando e, por padrão, começara em: http://127.0.0.1:5000/

## Testes
No repositório se encontra um arquivo de collection do Postman para testes.
Nesses testes, todas as frentes do CRUD são exploradas. Basta importar essa collection no Postman e executar os requests com o projeto já rodando.

## Documentação
Para a visualização da documentação Swagger:
No navegador, vá para "localhost:5000/swagger"
