from flask.ext.script import Manager
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)

manager = Manager(app)

if __name__ == "__main__":
    manager.run()
