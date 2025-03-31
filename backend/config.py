import os
from datetime import timedelta
from dotenv import load_dotenv

load_dotenv()

class Config:
    # Configurações gerais
    SECRET_KEY = os.getenv("SECRET_KEY") # procuro a chave no .env
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY") # procuro a chave no .env
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=1)

    # Configurações de banco de dados
    SQLALCHEMY_DATABASE_URI = os.getenv(
        'DATABASE_URL', 
        'sqlite:///roadtrack.db'
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = True

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'

def get_config():
    env = os.getenv('FLASK_ENV', 'development')
    config_selector = {
        'development': DevelopmentConfig,
        'production': ProductionConfig,
        'testing': TestingConfig
    }
    return config_selector.get(env, DevelopmentConfig) 