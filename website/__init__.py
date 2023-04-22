from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

db = SQLAlchemy()

DB_NAME = 'database.db'

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'mdfug3uygt43ugtu48734by43y'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)


    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    # do not remove this because we have to make sure models file should
    # run before the creation of the database
    from .models import User, Note

    with app.app_context():
        db.create_all()

     # this basically manages all the login functionality 
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login' # this tells if user is not logged in where we should redirect him/her
    login_manager.init_app(app) # this tells manager which app we are using 

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app

