from app import db


class Songs(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    artist = db.Column(db.String)
    year = db.Column(db.Integer)

    def __init__(self, title, artist, year):
        self.title = title
        self.artist = artist
        self.year = year

    def __repr__(self):
        return '<Song %r>' % self.title
