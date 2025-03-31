from flask import jsonify, request
from flask_jwt_extended import create_access_token, get_jwt_identity
from app.models import db, User
from app.models.password_reset import PasswordReset
from app.validators.auth_validator import validate_registration, validate_login
from app.services.email_service import send_reset_password_email

class AuthController:
    @staticmethod
    def register():
        data = request.get_json()

        # Validações de entrada
        if not data:
            return jsonify({"error": "Nenhum dado fornecido"}), 400

        name = data.get('name')
        email = data.get('email')
        password = data.get('password')

        # Validar dados de registro
        validation_errors = validate_registration(name, email, password)
        if validation_errors:
            return jsonify({"errors": validation_errors}), 400

        # Verificar se email já existe
        if User.query.filter_by(email=email).first():
            return jsonify({"error": "Email já cadastrado"}), 409

        # Criar novo usuário
        new_user = User(name=name, email=email)
        new_user.set_password(password)

        try:
            # Salvar usuário no banco de dados
            db.session.add(new_user)
            db.session.commit()

            # Gerar token JWT
            access_token = create_access_token(identity=new_user.id)

            return jsonify({
                "message": "Usuário registrado com sucesso",
                "user": new_user.to_dict(),
                "access_token": access_token
            }), 201

        except Exception as e:
            db.session.rollback()
            return jsonify({"error": "Erro ao registrar usuário", "details": str(e)}), 500
    # Login
    @staticmethod
    def login():
        data = request.get_json()

         # Validar dados de entrada
        validation_errors = validate_login(data)
        if validation_errors:
            return jsonify({"errors": validation_errors}), 400
    
        email = data.get('email')
        password = data.get('password')
    
         # Verificar se usuário existe
        user = User.query.filter_by(email=email).first()
        if not user:
            return jsonify({"error": "Usuário não encontrado"}), 404
    
        # Verificar senha
        if not user.check_password(password):
            return jsonify({"error": "Credenciais inválidas"}), 401
    
        # Gerar token de acesso
        access_token = create_access_token(identity=user.id)
    
        return jsonify({
            "access_token": access_token,
            "user": {
            "id": user.id,
            "name": user.name,
            "email": user.email
            }
        }), 200
    
    # atualizar dados
    @staticmethod
    def update_user( ):
        # Recuperar o id do usuário a partir do token JWT
        user_id = get_jwt_identity()
        data = request.json

        # Verificar se algum dado foi enviado
        if not data:
            return jsonify({"message": "Nenhum dado foi enviado para atualização"}), 400

        # Buscar o usuário no banco
        user = User.query.get(user_id)
        if not user:
            return jsonify({"message": "Usuário não encontrado"}), 404

        # Flag para verificar se pelo menos um campo válido foi atualizado
        updated = False

        # Verificar e processar apenas campos com valores válidos
        if "name" in data and data["name"] and data["name"].strip():
            user.name = data["name"]
            updated = True
    
        if "email" in data and data["email"] and data["email"].strip():
            # Verificar se o email já existe para outro usuário
            existing_user = User.query.filter(User.email == data["email"], User.id != user_id).first()
            if existing_user:
                return jsonify({"message": "Este email já está em uso por outro usuário"}), 422
            user.email = data["email"]
            updated = True
    
        if "password" in data and data["password"] and data["password"].strip():
            user.set_password(data["password"])
            updated = True
    
        # Se nenhum campo foi atualizado
        if not updated:
            return jsonify({"message": "Pelo menos um campo válido (name, email ou password) deve ser fornecido"}), 422
    
        # Salvar alterações
        try:
            db.session.commit()
            return jsonify({
                "message": "Usuário atualizado com sucesso!",
                "error": None
            }), 200
        except Exception as e:
            db.session.rollback()
            return jsonify({
                "message": f"Erro ao atualizar usuário: {str(e)}",
                "error": "Internal Server Error"
            }), 500
        
    # deletar conta 
    @staticmethod
    def delete_user():
        #obtem usuario autentificado atravez do token jwt
        current_user_id = get_jwt_identity()
        user = User.query.get(current_user_id)

        if not user:
            return jsonify({"error": "Usuário não encontrado"}), 404
    
        # Obtém os dados da requisição
        data = request.get_json()
    
        # Verifica se a senha foi fornecida para confirmar a exclusão
        password = data.get('password')
        if not password:
            return jsonify({"error": "Senha é necessária para confirmar a exclusão"}), 400
    
        # Validação da senha
        if not user.check_password(password):
            return jsonify({"error": "Credenciais inválidas"}), 401
    
        # Processa a exclusão
        try:        
           # Exclui o usuário
            db.session.delete(user)
            db.session.commit()
        
            return jsonify({
                "message": "Conta excluída permanentemente",
                "deleted_user": user.to_dict()  
            }), 200
        except Exception as e:
            db.session.rollback()
            return jsonify({
            "error": "Falha ao excluir conta",
            "details": str(e)
            }), 500


    # resete de senha
    @staticmethod
    def request_password_reset():

        data = request.get_json()
        # Validar dados de entrada
        validation_errors = validate_login(data)
        if validation_errors:
            return jsonify({"errors": validation_errors}), 400
    
        email = data.get('email')
        # Verificar se usuário existe
        user = User.query.filter_by(email=email).first()
        if not user:
            return jsonify({"error": "Usuário não encontrado"}), 404
        # Gera um novo token
        password_reset = PasswordReset.generate_token(user.email)
        
        # Envia o email com o link para redefinição
        reset_url = f"{request.host_url}reset-password?token={password_reset.token}"
        send_reset_password_email(user.email, reset_url)
        
        return jsonify({"message": "Email de redefinição de senha enviado com sucesso"}), 200

