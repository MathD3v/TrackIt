#TrackIt
Descrição do Projeto
O TrackIt é uma aplicação web que oferece funcionalidades de rastreamento e gestão de atividades para os usuários. O projeto foi desenvolvido utilizando o Flask (framework Python) e implementa a autenticação via JWT (JSON Web Tokens) para garantir a segurança nas comunicações entre o cliente e o servidor.

Tecnologias Utilizadas
Backend: Flask (Python)

Banco de Dados: SQLAlchemy (SQLite)

Autenticação: JWT (JSON Web Token)

Envio de E-mails: SMTP (para envio de e-mails de confirmação e redefinição de senha) - em andamento

Outras Dependências:

Flask-JWT-Extended

Flask-SQLAlchemy

Flask-Mail

Marshmallow (para validação de dados)

Flask-RESTful

Funcionalidades Principais
Cadastro de usuário: O usuário pode se cadastrar utilizando seu e-mail e senha.

Login com JWT: O usuário realiza o login e recebe um token JWT, que será utilizado para autenticar suas requisições.

Redefinição de Senha: O usuário pode solicitar uma redefinição de senha através do envio de um e-mail com um link contendo um token de redefinição. - em andamento

Proteção das rotas: Algumas rotas são protegidas, ou seja, o usuário precisa estar autenticado com o JWT para acessá-las.

Fluxo de Autenticação
Cadastro: O usuário se registra com e-mail e senha.

Login: Após o cadastro, o usuário pode realizar o login, que retorna um token JWT.

Acesso às rotas protegidas: O token JWT é enviado pelo cliente em cada requisição para acessar rotas protegidas.

Redefinir Senha: Caso o usuário esqueça a senha, ele pode solicitar uma redefinição, recebendo um link com um token temporário.

Instalação
Clone o repositório:
git clone https://github.com/seu-usuario/trackit.git

Crie e ative o ambiente virtual:
`python -m venv venv`
`.\venv\Scripts\activate`
Linux/macOS:
Instale as dependências:
`pip install -r requirements.txt`

Configuração do Banco de Dados: O projeto usa o SQLAlchemy para o banco de dados. Se for a primeira vez que você está configurando o projeto, rode os seguintes comandos para criar as tabelas:
`flask db init`
`flask db migrate`
`flask db upgrade`
Executar o servidor:
`flask run`
A aplicação estará disponível em http://127.0.0.1:5000/.

Rotas da API
Cadastro de usuário
POST /register
Descrição: Registra um novo usuário com e-mail e senha.
Body:

json
Copiar
{
  "email": "usuario@dominio.com",
  "password": "senhaSegura"
}
Login
POST /login
Descrição: Realiza o login do usuário e retorna um token JWT.
Body:

json
Copiar
{
  "email": "usuario@dominio.com",
  "password": "senhaSegura"
}
Redefinir Senha
POST /request-password-reset
Descrição: Solicita a redefinição de senha e envia um link com o token para o e-mail do usuário.
Body:

json
Copiar
{
  "email": "usuario@dominio.com"
}
Rota protegida
GET /protected-route
Descrição: Rota protegida, só acessível com um token JWT válido.
Headers:

bash
Copiar
Authorization: Bearer <token_jwt>
Exemplo de Resposta (Login)
Status: 200 OK

Body:

json
Copiar
{
  "access_token": "seu_token_jwt_aqui"
}
Possíveis Melhorias
Implementar a validação de e-mail para garantir que o e-mail fornecido seja válido e único.

Adicionar uma funcionalidade de "lembrar-me" para manter o usuário autenticado por mais tempo.

Melhorar a segurança com o uso de variáveis de ambiente para armazenar chaves secretas e configurações sensíveis.")
