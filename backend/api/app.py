from flask import Flask
from database.db import db
from envs import SQLALCHEMY_DATABASE_URI


def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI

    db.init_app(app)

    return app


app = create_app()
