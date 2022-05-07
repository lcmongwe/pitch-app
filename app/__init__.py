import re
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


db = SQLAlchemy()
DB_NAME ='pitches.db'


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'topsec'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://lucy:4444@localhost/pitches'
    db.init_app(app)

    login_manager=LoginManager()
    login_manager.login.view ="auth.login"
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    from ..views import views
    from .auth import auth

    app.register_blueprint(views,url_prefix='/')
    app.register_blueprint(auth,url_prefix='/')

    from .models import User, Note

    # create_database(app)

    return app

# def create_database(app):
#     if not path.exists('app/'):
#         db.create_all(app=app)
#         print('created database')