from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from app.routes.auth import auth_bp
from app.models.user import db

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')

    db.init_app(app)
    with app.app_context():
        db.create_all()
    CORS(app, supports_credentials=True)
    app.register_blueprint(auth_bp)

    return app
print("create_app function executed")
