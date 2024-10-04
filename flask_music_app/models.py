from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
class Artist(db.model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    genre = db.column(db.string(100), nullable=False)
    music = db.relationship('music', backref='artist', lazy=True)

    class music(db.model):
        id