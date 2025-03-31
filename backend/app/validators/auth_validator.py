import re

def validate_registration(name, email, password):
    errors = []
    
    if not name or not name.strip():
        errors.append("Nome é obrigatório")
    
    if not email or not email.strip():
        errors.append("Email é obrigatório")
    elif not re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", email):
        errors.append("Email inválido")
    
    if not password:
        errors.append("Senha é obrigatória")
    elif len(password) < 8:
        errors.append("Senha deve ter pelo menos 8 caracteres")
    
    return errors

def validate_login(data):
    errors = []
    
    if not data:
        errors.append("Dados de login são obrigatórios")
        return errors
    
    email = data.get('email')
    password = data.get('password')
    
    if not email or not email.strip():
        errors.append("Email é obrigatório")
    
    if not password:
        errors.append("Senha é obrigatória")
    
    return errors
