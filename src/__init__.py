from flask import Flask

# Routes
from src import index
from src.routes import collection_rout, products, user, auth

app = Flask(__name__)

def init_app(config):
    # Configuration
    app.config.from_object(config)

    # Blueprints
    app.register_blueprint(index.index_bp, url_prefix='/')
    app.register_blueprint(auth.auth_bp, url_prefix='/api/auth')
    app.register_blueprint(user.user_bp, url_prefix='/api/users')
    app.register_blueprint(products.product_bp, url_prefix='/api/products')
    #app.register_blueprint(collection.collection_bp, url_prefix='/api/collection')

    return app