from collections import namedtuple
from random import choice

from flask import Flask, jsonify

Quote = namedtuple("Quote", ("text", "author"))

quotes = [ 
        Quote("Help me, Obi-Wan Kenobi", "Leia"),
        Quote("It's not my fault", "Han Solo"),
        Quote("Do. Or do not. There is no try.", "Yoda"),
        Quote("I find your lack of faith disturbing.", "Darth Vader"),
        Quote("Never tell me the odds", "Han Solo")
]


app = Flask(__name__)

@app.route('/', methods=['GET'])
def get_random_quote():
    return jsonify(choice(quotes)._asdict())


if __name__ == '__main__':
    app.run()

