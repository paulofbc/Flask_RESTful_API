# Importação de Bibliotecas
from flask import Flask, request, Response, jsonify
from flask_sqlalchemy import SQLAlchemy


# Criação de uma instância para a aplicação Flask
app = Flask(__name__)

# Configuração do Banco de Dados
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
