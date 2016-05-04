from T1SS import db


class UsedWord(db.Model):
    __tablename__ = 'used_words'
    id = db.Column(db.Integer, primary_key=True)
    word = db.Column(db.String(160))
    user_name_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __init__(self, word=None):
        self.word = word

    @staticmethod
    def store_if_no_exist(word, user):
        uw = UsedWord.query.filter(UsedWord.word == word, UsedWord.user_name_id == user.id).first()

        if not uw:
            uw = UsedWord(word=word)
            user.used_words.append(uw)
            db.session.add(uw)
            db.session.add(user)
            db.session.commit()
        return uw
