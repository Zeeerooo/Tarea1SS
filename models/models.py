from manage import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    word = db.Column(db.String(32), unique=True)
    mac = db.Column(db.String(150))
    key = db.Column(db.String(150), unique=True)
