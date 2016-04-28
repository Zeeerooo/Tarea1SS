from flask.ext.script import Manager, Server
from flask_migrate import Migrate, MigrateCommand
from T1SS import app, db

migrate = Migrate(app, db)

manager = Manager(app)

manager.add_command('db', MigrateCommand)
manager.add_command('runserver', Server(threaded=True))

if __name__ == "__main__":
    manager.run()

