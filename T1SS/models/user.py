from T1SS import db


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(32), unique=True)
    aes_key = db.Column(db.String(150), unique=True)
    validated = db.Column(db.Boolean)

    def __init__(self, id, user_name=None, aes_key=None):
        self.id = id
        self.user_name = user_name
        self.aes_key = aes_key
        self.validated = False

    def validateHomework(self):
        self.validated = True
