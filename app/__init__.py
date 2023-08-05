from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate = Migrate(app, db)  

    from app.routes import excel_routes, database_routes
    app.register_blueprint(excel_routes.bp)
    app.register_blueprint(database_routes.bp)

    return app
