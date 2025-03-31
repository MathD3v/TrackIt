# TrackIt - Sistema de Rastreamento com Autenticação JWT

**TrackIt** é um projeto desenvolvido com o objetivo de gerenciar o rastreamento de atividades. Ele implementa autenticação via JWT, garantindo um fluxo seguro de login, registro e verificação de autenticação em todas as rotas protegidas.

## Funcionalidades

- **Autenticação JWT**: Fluxo de login com geração de tokens JWT para autenticação nas requisições.
- **Criação e verificação de usuários**: Permite o registro de novos usuários e verificação de credenciais.
- **Proteção de rotas**: Algumas rotas exigem autenticação por meio de token JWT.
- **Banco de dados**: Utiliza o SQLAlchemy para persistir dados de usuários e registros.
  
## Tecnologias Utilizadas

- **Flask**: Framework web para desenvolvimento da API.
- **Flask-JWT-Extended**: Para trabalhar com autenticação e proteção de rotas com tokens JWT.
- **Flask-SQLAlchemy**: ORM para interagir com o banco de dados.
- **Flask-Migrate**: Para migrações de banco de dados.
- **Werkzeug**: Para depuração e execução em ambiente de desenvolvimento.

## Pré-requisitos

Certifique-se de ter o Python instalado e um ambiente virtual configurado.

### Instalando dependências

1. **Clone o repositório**:
    ```bash
    git clone https://github.com/usuario/trackit.git
    cd trackit
    ```

2. **Crie e ative o ambiente virtual**:
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # no Linux/macOS
    .venv\Scripts\activate  # no Windows
    ```

3. **Instale as dependências**:
    ```bash
    pip install -r requirements.txt
    ```

## Como rodar a aplicação

### Rodando a aplicação

1. **Inicie o banco de dados e aplicação** (caso ainda não tenha feito):
    ```bash
    python run.py
    ```

   O servidor Flask estará rodando no `localhost` na porta padrão `5000`. A aplicação estará em modo de depuração (modo `debug=True`), permitindo detectar mudanças automaticamente no código.

### Arquivo `run.py`

O `run.py` é responsável por iniciar o servidor da aplicação e garantir que o banco de dados seja inicializado corretamente.

### Documento sobre api na pasta document_api
- ** Documentado pelo postman
- ** Instale o postman
- ** import o projeto
