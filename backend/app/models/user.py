from app import db
from datetime import datetime, timedelta
from werkzeug.security import generate_password_hash, check_password_hash
import secrets
from sqlalchemy.sql import func

class User(db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def set_password(self, password):
        """Criar hash da senha"""
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        """Verificar senha"""
        return check_password_hash(self.password_hash, password)

    def to_dict(self):
        """Converter modelo para dicionário"""
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'created_at': self.created_at.isoformat()
        }

    @classmethod
    def generate_token(cls, user_id, expires_in=3600):
        """Gera um novo token para redefinição de senha"""
        token = secrets.token_urlsafe(64)
        expires_at = datetime.utcnow() + timedelta(seconds=expires_in)
        
        # Invalida tokens anteriores para este usuário
        cls.query.filter_by(user_id=user_id, used=False).update({'used': True})
        
        # Cria um novo token
        reset = cls(
            user_id=user_id,
            token=token,
            expires_at=expires_at
        )
        db.session.add(reset)
        db.session.commit()
        
        return reset
    
    @classmethod
    def verify_token(cls, token):
        """Verifica se o token é válido e retorna o objeto de redefinição de senha"""
        reset = cls.query.filter_by(
            token=token,
            used=False
        ).first()
        
        if not reset:
            return None
            
        if reset.expires_at < datetime.utcnow():
            reset.used = True
            db.session.commit()
            return None
            
        return reset
        
    def use_token(self):
        """Marca o token como usado"""
        self.used = True
        db.session.commit()
