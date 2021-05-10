from settings import *
import json


# Inicializando o banco de dados
db = SQLAlchemy(app)


# A classe Movie irá herdar o db.Model do SQLAlchemy
class Movie(db.Model):
    __tablename__ = 'movies'  # Criando o nome da tabela
    id = db.Column(db.Integer, primary_key=True)  # Atributo identificador
    title = db.Column(db.String(80), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    genre = db.Column(db.String(80), nullable=False)

    # Método de tradução da saída (output) para json
    def json(self):
        return {'id': self.id, 'title': self.title,
                'year': self.year, 'genre': self.genre}

    # Função que adiciona um novo filme no banco de dados
    def add_movie(_title, _year, _genre):
        # Criação de uma instância do construtor do Movie
        new_movie = Movie(title=_title, year=_year, genre=_genre)
        db.session.add(new_movie)  # Adiciona novo filme para a sessão do banco de dados
        db.session.commit()  # Realiza o commit da sessão

    # Função de busca por todos os filmes
    def get_all_movies():
        return [Movie.json(movie) for movie in Movie.query.all()]

    # Função de busca de filme por id
    def get_movie(_id):
        return [Movie.json(Movie.query.filter_by(id=_id).first())]

    # Função de atualização dos atributos do filme
    def update_movie(_id, _title, _year, _genre):
        movie_to_update = Movie.query.filter_by(id=_id).first()
        movie_to_update.title = _title
        movie_to_update.year = _year
        movie_to_update.genre = _genre
        db.session.commit()

    # Função de remoção de um filme do banco de dados
    def delete_movie(_id):
        Movie.query.filter_by(id=_id).delete()
        # Filtra por id + delete()
        db.session.commit()
        