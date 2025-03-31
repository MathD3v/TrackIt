from flask import Blueprint
from flask_jwt_extended import jwt_required
from app.controllers.auth_controller import AuthController

auth_bp = Blueprint('auth', __name__, url_prefix='/user')

@auth_bp.route('user/register', methods=['POST'])
def register():
    return AuthController.register()

@auth_bp.route('user/login', methods=['POST'])
def login():
    return AuthController.login()

@auth_bp.route('user/update_user', methods=['PUT'])
@jwt_required()
def update_user():
    return AuthController.update_user()

@auth_bp.route('user/delete_user', methods=['DELETE'])
@jwt_required()
def delete_user():
    return AuthController.delete_user()

@auth_bp.route('user/esquecer-senha/<int:user_id>', methods=['POST'])
def forgot_password(user_id):
    return AuthController.request_password_reset(user_id)

@auth_bp.route('user/redefinir-senha', methods=['POST'])
def reset_password():
    return AuthController.update_user()