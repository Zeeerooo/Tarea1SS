from T1SS import db


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(32), unique=True)
    aes_key = db.Column(db.String(150), unique=True)
    validated = db.Column(db.Boolean)
    used_words = db.relationship('UsedWord', backref='user',
                                 lazy='dynamic')

    def __init__(self, user_name=None, aes_key=None):
        self.user_name = user_name
        self.aes_key = aes_key
        self.validated = False

    def validateHomework(self):
        self.validated = True
        db.session.add(self)
        db.session.commit()
