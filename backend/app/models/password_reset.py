from datetime import datetime, timedelta
import secrets
from sqlalchemy.sql import func
from app.models import db
from flask import request, jsonify


class PasswordReset(db.Model):
    __tablename__ = 'password_resets'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    token = db.Column(db.String(100), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=func.now())
    expires_at = db.Column(db.DateTime, nullable=False)
    used = db.Column(db.Boolean, default=False)
    
    @staticmethod
    def request_password_reset():
        try:
            # Obter dados da requisição
            data = request.get_json()
            
            # Validar dados de entrada
            validation_errors = validate_login(data)
            if validation_errors:
                return jsonify({"errors": validation_errors}), 400
            
            email = data.get('email')

            # Verificar se o usuário existe
            user = User.query.filter_by(email=email).first()
            if not user:
                return jsonify({"error": "Usuário não encontrado"}), 404

            # Gera um novo token com validade de 5 minutos
            password_reset = PasswordReset.generate_token(user.email)

            # Enviar o e-mail com o link para redefinição
            reset_url = f"{request.host_url}reset-password?token={password_reset.token}"
            send_reset_password_email(user.email, reset_url)
            
            return jsonify({"message": "Email de redefinição de senha enviado com sucesso"}), 200
        except Exception as e:
            # Erro inesperado
            return jsonify({"error": f"Erro interno: {str(e)}"}), 500
        
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
