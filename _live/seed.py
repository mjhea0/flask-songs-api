from models import Songs
from app import db

song = Songs('Can\'t stop', 'Red Hot Chili Peppers', 1970)

db.session.add(song)
db.session.commit()
