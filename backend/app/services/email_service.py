from flask_mail import Message
from app import mail

def send_reset_password_email(email, reset_url):
    """Serviço para envio de email de redefinição de senha"""
    msg = Message(
        'Redefinição de Senha',
        recipients=[email]
    )
    
    msg.body = f"""
    Olá,
    
    Você solicitou a redefinição de sua senha. Para continuar, clique no link abaixo:
    
    {reset_url}
    
    Este link expirará em 1 hora.
    
    Se você não solicitou esta redefinição, por favor ignore este email.
    
    Atenciosamente,
    Equipe de Suporte
    """
    
    msg.html = f"""
    <h2>Redefinição de Senha</h2>
    <p>Olá,</p>
    <p>Você solicitou a redefinição de sua senha. Para continuar, clique no link abaixo:</p>
    <p><a href="{reset_url}">Redefinir minha senha</a></p>
    <p>Este link expirará em 1 hora.</p>
    <p>Se você não solicitou esta redefinição, por favor ignore este email.</p>
    <p>Atenciosamente,<br>Equipe de Suporte</p>
    """
    
    mail.send(msg)
