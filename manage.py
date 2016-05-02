from flask.ext.script import Manager, Server

import os
from T1SS import app, db
from T1SS.static.people import people
from flask_migrate import Migrate, MigrateCommand
from sqlalchemy.exc import IntegrityError

migrate = Migrate(app, db)

manager = Manager(app)

manager.add_command('db', MigrateCommand)
manager.add_command('runserver', Server(threaded=True))


@manager.command
def populate():
    import json
    from T1SS.models.user import User
    jsonvar = json.loads(people)
    for k, v in jsonvar.items():
        if k == "users":
            for json_element in v:
                model = User()
                for k, v in json_element.items():
                    setattr(model, k, v)
                model.aes_key = str(os.urandom(16))

                db.session.add(model)
                try:
                    db.session.commit()
                except IntegrityError:
                    db.session.rollback()


from T1SS import public

if __name__ == "__main__":
    manager.run()
