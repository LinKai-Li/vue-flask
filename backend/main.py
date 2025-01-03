from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)

app.config.from_object(__name__)

CORS(app, resources={r'/*': {'origins': '*'}})

# hello world route
@app.route('/', methods=['GET'])
def greetings():
    return("Hello, world!")

@app.route('/shark', methods=['GET'])
def shark():
    return("Shark!")

GAMES = [
    {
        'title': '2k21',
        'genre': 'sports',
        'played': True,
    },
    {
        'title': 'Evil Within',
        'genre': 'horror',
        'played': False,
    },
    {
        'title': 'the last of us',
        'genre': 'survival',
        'played': True,
    },
    {
        'title': 'days gone',
        'genre': 'horror/survival',
        'played': False,
    },
    {
        'title': 'mario',
        'genre': 'retro',
        'played': True,
    },
]

# The GET route handler
@app.route('/games', methods=['GET'])
def all_games():
    return jsonify({
        'games': GAMES,
        'status': 'success'
    })

if __name__ == '__main__':
    app.run(debug=True, port=8000)