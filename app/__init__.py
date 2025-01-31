from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path

db = SQLAlchemy()
DB_NAME = "hndb.db"

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'huiasgdnkbq123421lj4kbn'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    from .views import views

    app.register_blueprint(views, url_prefix ='/')

    from .models import Product
    create_database(app)

    return app

def create_database(app):
    if not path.exists('app/' + DB_NAME):
        with app.app_context():
            db.create_all()
        print('Created DB!')