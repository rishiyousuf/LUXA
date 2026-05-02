from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy()

def create_app(config_name='development'):
    app = Flask(__name__)
    
    # Load configuration
    from config import config
    app.config.from_object(config[config_name])
    
    # Initialize database
    db.init_app(app)
    
    # Register blueprints
    from app.routes import main, products, cart, auth, admin
    app.register_blueprint(main.bp)
    app.register_blueprint(products.bp)
    app.register_blueprint(cart.bp)
    app.register_blueprint(auth.bp)
    app.register_blueprint(admin.bp)
    
    # Create tables
    with app.app_context():
        db.create_all()
    
    return app
