from flask import Flask

# Import extensions
from .extensions import bcrypt, cors, db, jwt, ma


def create_app():
    app = Flask(__name__)
    app.config.from_object("config.DevelopmentConfig")

    register_extensions(app)

    # # Register blueprints
    # from .auth import auth_bp

    # app.register_blueprint(auth_bp)

    # from .api import api_bp

    # app.register_blueprint(api_bp, url_prefix="/api")
    @app.route('/hello')
    def hello():
        return 'Hello, World!'
    return app


def register_extensions(app):
    # Registers flask extensions
    db.init_app(app)
    # ma.init_app(app)
    jwt.init_app(app)
    bcrypt.init_app(app)
    # cors.init_app(app)