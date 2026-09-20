from flask import Flask
from flask_cors import CORS
from extensions import db
from config import Config
import routes


def create_app():
    app = Flask(__name__)       
    app.config.from_object(Config)
    CORS(app)
    db.init_app(app)
    with app.app_context():

        from models import Product

        db.create_all()
    app.register_blueprint(routes.products_routes)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True, port=5000)
