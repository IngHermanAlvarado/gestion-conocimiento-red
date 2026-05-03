from flask import Flask
import os

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-secret-key')
    
    from app.routes import main_bp
    app.register_blueprint(main_bp)
    
    return app
