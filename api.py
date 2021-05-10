from movies import *
from flask_swagger_ui import get_swaggerui_blueprint


# Route para busca de todos os filmes
@app.route('/movies', methods=['GET'])
def get_movies():
    return jsonify({'Movies': Movie.get_all_movies()})


# Route de busca de filmes através da id
@app.route('/movies/<int:id>', methods=['GET'])
def get_movie_by_id(id):
    return_value = Movie.get_movie(id)
    return jsonify(return_value)


# Route que adiciona novo filme
@app.route('/movies', methods=['POST'])
def add_movie():
    request_data = request.get_json()  # Coletando dados do cliente
    Movie.add_movie(request_data["title"], request_data["year"],
                    request_data["genre"])
    response = Response("Filme Adicionado!", 201, mimetype='application/json')
    return response


# Route para atualizar um filme
@app.route('/movies/<int:id>', methods=['PUT'])
def update_movie(id):
    request_data = request.get_json()
    Movie.update_movie(id, request_data['title'], request_data['year'], request_data['genre'])
    response = Response("Filme Atualizado!", status=200, mimetype='application/json')
    return response


# Route para deletar um filme
@app.route('/movies/<int:id>', methods=['DELETE'])
def remove_movie(id):
    Movie.delete_movie(id)
    response = Response("Filme Deletado!", status=200, mimetype='application/json')
    return response


# Configuração do Swagger
SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.yaml'

SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        "app_name": "Product API"
    }
)

app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)


if __name__ == "__main__":
    app.run(port=5000, debug=True)
