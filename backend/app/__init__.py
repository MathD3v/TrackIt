from flask import Flask
from flask_jwt_extended import JWTManager
from flask_mail import Mail
from app.models import db

# Inicialização de extensões
jwt = JWTManager()
mail = Mail()

def create_app(config_class=None):
    # Criar aplicação Flask
    app = Flask(__name__)
    
    # Importar configurações
    from config import get_config
    config_class = config_class or get_config()
    app.config.from_object(config_class)
    
    # Inicializar extensões
    db.init_app(app)
    jwt.init_app(app)
    mail.init_app(app)
    
    # Importar e registrar blueprints
    from .routes.auth_routes import auth_bp
    app.register_blueprint(auth_bp, url_prefix='/api')
    
    # Criar as tabelas do banco de dados
    with app.app_context():
        db.create_all()
    
    return app