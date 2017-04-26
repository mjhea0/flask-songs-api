# dependencies
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

# app config
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://localhost:5432/songs'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

import models


# routes
@app.route('/api/v1/songs', methods=['GET'])
def index():
    all_data = []
    songs = models.Songs.query.all()
    for song in songs:
        all_data.append({
            'title': song.title,
            'artist': song.artist,
            'year': song.year
        })
    return jsonify(all_data)


if __name__ == '__main__':
    app.debug = True
    app.run()
