import re

def validate_email(email):
    """Validar formato de email"""
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(email_regex, email) is not None

def validate_registration(name, email, password):
    """Validar dados de registro"""
    errors = []

    if not name or len(name.strip()) < 2:
        errors.append("Nome deve ter no mínimo 2 caracteres")
    
    if not email:
        errors.append("Email é obrigatório")
    elif not validate_email(email):
        errors.append("Formato de email inválido")
    
    if not password or len(password) < 6:
        errors.append("Senha deve ter no mínimo 6 caracteres")
    
    return errors

def validate_login(data):
    errors = []
    
    # Verificar se dados foram enviados
    if not data:
        return ["Nenhum dado fornecido"]
    
    # Validar email
    email = data.get('email', '').strip()
    if not email:
        errors.append("Email é obrigatório")
    elif '@' not in email:
        errors.append("Email inválido")
    
    # Validar senha
    password = data.get('password', '')
    if not password:
        errors.append("Senha é obrigatória")
    elif len(password) < 6:
        errors.append("Senha deve ter no mínimo 6 caracteres")
    
    return errors