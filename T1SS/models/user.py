from T1SS import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(32), unique=True)
    ex_word = db.Column(db.String(32), unique=True)
    ex_mac = db.Column(db.String(150))
    aes_key = db.Column(db.String(150), unique=True)
    validated = db.Column(db.Boolean)

    def __init__(self, id, user_name, ex_word, ex_mac, aes_key):
        self.id = id
        self.user_name = user_name
        self.ex_word = ex_word
        self.ex_mac = ex_mac
        self.aes_key = aes_key
        self.validated = False

    def validateHomework(self):
        self.validated = True
