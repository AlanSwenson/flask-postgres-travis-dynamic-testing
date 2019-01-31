from flask import Flask, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

from project.config import Config

db = SQLAlchemy()

# App Factory
def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    with app.app_context():
        db.init_app(app)
        register_blueprints(app)

    @app.route("/", methods=["POST", "GET"])
    def root():
        return redirect(url_for("main.index"))

    return app


def register_blueprints(app):
    from project.main.views import main_blueprint

    app.register_blueprint(main_blueprint, url_prefix="/main")
