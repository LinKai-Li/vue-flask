from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import uuid

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///game.db'
db = SQLAlchemy(app)

CORS(app, resources={r'/*': {'origins': '*'}})

class Game(db.Model):
    id = db.Column(db.String(36), primary_key=True)
    title = db.Column(db.String(80), unique=True, nullable=False)
    genre = db.Column(db.String(80), unique=True, nullable=False)
    played = db.Column(db.Boolean, unique=False, nullable=False)

    def __init__(self, title, genre, played):
        self.id = uuid.uuid4().hex
        self.title = title
        self.genre = genre
        self.played = played

with app.app_context():
    db.create_all()

# hello world route
@app.route('/', methods=['GET'])
def greetings():
    return("Hello, world!")

@app.route('/shark', methods=['GET'])
def shark():
    return("Shark!")

# The GET and POST route handler
@app.route('/games', methods=['GET', 'POST'])
def all_games():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        new_game = Game(
            title=post_data.get('title'),
            genre=post_data.get('genre'),
            played=post_data.get('played')
        )
        db.session.add(new_game)
        db.session.commit()
        response_object['message'] = 'Game Added!'
        response_object['game'] = {
            'id': new_game.id,
            'title': new_game.title,
            'genre': new_game.genre,
            'played': new_game.played
        }
    else:
        games = Game.query.all()
        response_object['games'] = [
            {
                'id': game.id,
                'title': game.title,
                'genre': game.genre,
                'played': game.played
            } for game in games
        ]
    return jsonify(response_object)

# The PUT and DELETE route handler
@app.route('/games/<game_id>', methods=['PUT', 'DELETE'])
def single_game(game_id):
    response_object = {'status': 'success'}
    if request.method == "PUT":
        post_data = request.get_json()
        game = Game.query.filter_by(id=game_id).first()
        if game:
            game.title = post_data.get('title')
            game.genre = post_data.get('genre')
            game.played = post_data.get('played')
            db.session.commit()
            response_object['message'] = 'Game Updated!'
            response_object['game'] = {
                'id': game.id,
                'title': game.title,
                'genre': game.genre,
                'played': game.played
            }
        else:
            response_object['status'] = 'failure'
            response_object['message'] = 'Game not found!'
    elif request.method == "DELETE":
        game = Game.query.filter_by(id=game_id).first()
        if game:
            db.session.delete(game)
            db.session.commit()
            response_object['message'] = 'Game Deleted!'
        else:
            response_object['status'] = 'failure'
            response_object['message'] = 'Game not found!'
    return jsonify(response_object)

if __name__ == '__main__':
    app.run(debug=True, port=8000)