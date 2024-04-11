from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from app import pages


def create_app():
    app = Flask(__name__, template_folder='templates/pages')
    app = Flask(__name__, template_folder='templates')
    app.secret_key = "@secretkey#"
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    class Base(DeclarativeBase):
        pass
    db = SQLAlchemy(model_class=Base)

    app.register_blueprint(pages.bp)
    return app
